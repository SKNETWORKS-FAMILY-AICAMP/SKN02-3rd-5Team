from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import BaseOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# url을 통해서 pdf 정보 가져오기
loader = PyPDFLoader("data/product_guide.pdf")
pages = loader.load_and_split()
pages[0]

# PDF 내용을 작은 chunk 단위로 나누기
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
splits = text_splitter.split_documents(pages)

# OpenAI Embedding 모델을 이용해서 Chunk를 Embedding 한후 Vector Store에 저장
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=openai_api_key)) # text-embedding-ada-002
retriever = vectorstore.as_retriever(search_kwargs={'k':10})

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, openai_api_key=openai_api_key)

### Contextualize question ###
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

# Chain 영역
class OutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""


    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split("\n")

class RagChainGenerator():
    def __init__(self):
        self.template = ""
        self.ragchain = self.rag_chain_generator()
        self.store = {}

    def template_generator(self):
        template_text = f"""
                You are an assistant for question-answering tasks.
                Use the following pieces of retrieved context to answer the question.
                Answer step by step with a kind tone.
                If you don't know the answer, tell them to contact the customer center directly.
                Never try to make up an answer.
                The user doesn't have a manual, so don't ask him to look at it.
                Always say 'thank you for your questions!' at the end of your response.
                \n\n
                """
        return template_text + """
                {context}
                질문: {input}
                You MUST answer in Korean:
                """
    
    def prompt_generator(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.template_generator()),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}")
        ])
        return prompt
    
    def rag_chain_generator(self):
        question_answer_chain = create_stuff_documents_chain(llm, self.prompt_generator())
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
        return RunnableWithMessageHistory(
            rag_chain,
            self.get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
            )
    
    # 세션 ID를 기반으로 세션 기록을 가져오는 함수
    def get_session_history(self, session_ids):
        if session_ids not in self.store:  # 세션 ID가 store에 없는 경우
            # 새로운 ChatMessageHistory 객체를 생성하여 store에 저장
            self.store[session_ids] = ChatMessageHistory()
        return self.store[session_ids]  # 해당 세션 ID에 대한 세션 기록 반환

rcg = RagChainGenerator()

# RAG chain 설정
def result_return(text, session_id):
    rag_chain = rcg.ragchain
    
    result = rag_chain.invoke(
        {"input": text}, 
            config = {"configurable": {"session_id": session_id}}
    )["answer"]

    return result