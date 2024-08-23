# SKN AI Camp 3차 프로젝트

## SKN02-3rd-5Team
<table>
  <tr>
    <th>구선아</th>
    <th>송문영</th>
    <th>서종호</th>
    <th>장정원</th>
  </tr>
  <tr>
    <td>
      <img src= "https://github.com/user-attachments/assets/06918eee-dcfb-40bd-89fb-a6d3de068047" 
                alt="Disgust" width="100" height="148"> 
    </td>

  <td>
      <img src= "https://github.com/user-attachments/assets/19543394-3a7f-4bf9-b120-257c53102f18" 
                alt="embarrassment" width="110" height="148">
  </td>
    
  <td>
      <img src= "https://github.com/user-attachments/assets/3573a236-ddd7-4a4c-94cd-b4a04cf3226a" 
                alt="Anxiety" width="100" height="148"> 
  </td>
  
  <td>
      <img src= "https://github.com/user-attachments/assets/b837713b-378d-4d7d-a2a4-e29a31d7dae0" 
                alt="Anger" width="100" height="148"> 
  </td>
  </tr>
  <tr>
    <td>@developer0826</td>
    <td>@MOONisYOUNG</td>
    <td>@Seo-jong-ho</td>
    <td>@jwjang1</td>
  </tr>
</table>

<br>

# Smart Manual: QR로 만나는 AI 사용설명서
Smart Manual: QR로 만나는 AI 사용설명서는 AI 기반의 대화형 사용자 매뉴얼입니다. 사용자가 궁금한 사항을 질문하면 AI가 실시간으로 답변을 제공하며. 이 프로젝트는 Streamlit을 사용하여 웹 애플리케이션을 구축하였으며, OpenAI의 언어 모델을 활용해 사용자와 자연스러운 대화를 이어나갑니다. 다양한 PDF 문서를 간단하게 처리하여 중요한 정보를 추출하고, 이를 바탕으로 사용자가 필요한 정보를 빠르고 정확하게 제공하는 것을 목표로 합니다.  

## 프로젝트 소개
이 프로젝트는 사용자의 간단한 접근으로 모델이 문서의 정보를 추출하여 가공하고 실시간으로 쉽게 대화할 수 있는 챗봇을 제공하는것을 목표로 설정하였습니다. 주제로 선정하게 된 배경은 사용자들이 메뉴얼을 읽는 불편함을 줄이고, 좀 더 상호작용적인 경험을 제공하기 위함입니다. 특히, RAG(Retrieval-Augmented Generation)(검색 - 생성 결합 모델) 기술을 활용하여 비용 효율적인 구현, 사용자의 신뢰 강화, 모델의 맥락 이해력을 향상 시킬 수 있는 답변을 제공하도록 구상하였습니다.

## 데이터
이 프로젝트에서 사용된 데이터는 SK매직 서비스 센터에서 제공하는 제품 사용 설명서 중, 특히 SK매직에서 가장 잘 판매되는 정수기 상품군의 설명서중 하나를 기반으로 수집되었습니다. 

![image](https://github.com/user-attachments/assets/ee1d7eca-1601-455a-ae5e-2f1b5760c9f5)


## 시스템 아키텍쳐
![image](https://github.com/user-attachments/assets/9a9cf6df-cdbd-47dc-afe0-14c6af269a4f)

## 테스트 및 개선 과정
### 1. **프롬프트 개선**
![image](https://github.com/user-attachments/assets/4144b1c2-2638-4214-827f-35f04d833d7e)
프롬프트를 보다 명확하고 구체적으로 개선하여, 모델이 사용자 질문을 더 잘 이해하고 정확한 답변을 제공할 수 있도록 최적화했습니다. 또한 환각 현상을 방지하기 위한 내용을 추가하여 검증되지 않고 제공되지 않은 문서 내용을 출력 하지 않도록 조정하였습니다. 또한 영문으로 수정하여 모델이 더욱 더 정확하게 해석하고 더 정확한 답변을 할 수 있도록 조정하였습니다.

### 2. **모델 명 입력 기능 제거**
![image](https://github.com/user-attachments/assets/5239704c-1571-4797-8f25-3731771c4cba)  
초기 시스템의 복잡성을 줄이고 사용자 경험을 단순화하기 위해 모델 선택 기능을 제거했습니다. 대신 모델을 확인이 필요한 상황에서 모델을 확인하는 과정을 추가하여, 사용자가 추가적인 선택 과정 없이 일관된 결과를 얻을 수 있도록 했습니다.

### 3. **히스토리 기능 추가**
![image](https://github.com/user-attachments/assets/eb8eb206-b046-4d30-808c-f7587625bbc1)  
사용자의 이전 대화 기록을 저장하고, 이를 반영하여 문맥을 유지한 응답을 제공하는 히스토리 기능을 추가했습니다. 이 기능은 대화의 일관성을 높이고, 더욱 자연스러운 사용자 경험을 가능하게 합니다.

## 개선점
이 프로젝트는 AI 기반의 스마트 사용자 매뉴얼 시스템을 성공적으로 구현했습니다. 그러나 향후 성능과 사용자 경험을 더욱 향상시키기 위해 다음과 같은 개선점을 고려할 수 있습니다.

### **1. 응답 속도 최적화**

- **효율적인 검색 구현**: 현재 시스템은 상위 10개의 관련 텍스트 청크를 검색하여 응답을 생성합니다. 하지만 데이터셋이 확장되거나 더 복잡한 쿼리가 추가될 경우, 응답 시간이 길어질 수 있습니다. 이 문제를 해결하기 위해 **벡터 데이터베이스의 인덱싱 최적화**와 **캐싱 전략**을 도입하여 검색 속도를 향상시킬 수 있습니다.
- **병렬 처리**: 사용자 질문에 대해 다중 스레드나 병렬 처리 기술을 적용하여 응답 생성 속도를 높일 수 있습니다. 이를 통해 복잡한 질문이나 대용량 데이터 처리 시에도 신속한 응답을 제공할 수 있습니다.

### **2. 모델 정확도 향상**

- **도메인 특화 학습**: 현재 모델의 성능을 더욱 강화하기 위해 SK매직 제품에 특화된 데이터를 추가로 수집하고 학습시키는 것이 필요합니다. 더 다양한 제품 설명서를 포함하거나 **멀티모달 데이터**(예: 이미지, 동영상)를 활용하여 모델의 이해도를 높일 수 있습니다.
- **데이터 증강**: 학습 데이터의 다양성을 높이기 위해 데이터 증강 기법을 적용할 수 있습니다. 동의어 치환이나 문장 순서 변경, 역번역, 섹션 순서 변경 등의 데이터 증강 기법을 활용하여 모델이 다양한 상황에서도 일관된 성능을 발휘하고 데이터 부족 문제를 해결 할 수 있습니다.

### **3. 사용자 피드백 기반 개선**

- **실시간 피드백 시스템 구축**: 사용자의 피드백을 실시간으로 수집하고 분석할 수 있는 시스템을 구축하여, 사용자가 경험하는 문제점을 즉각적으로 파악하고 개선할 수 있습니다. 예를 들어, 사용자 불만 사항을 분석하여 모델의 응답이나 UI/UX를 개선하는 데 활용할 수 있습니다.
- **지속적인 사용자 경험 개선**: 사용자 인터페이스와 상호작용을 지속적으로 개선하기 위해 정기적인 사용자 테스트를 실시하고, 이를 바탕으로 인터페이스를 업데이트합니다.

## Tech Stack

### Development Tools (개발 도구)
<img src="{https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue}" />

https://img.shields.io/badge/VSCode-2F80ED?style=for-the-badge&logo=codefactor&logoColor=white

https://img.shields.io/badge/GoogleColab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white

### Collaboration Tools (협업 도구)

https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=Discord&logoColor=white

https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white

https://img.shields.io/badge/GoogleDrive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white

### Version Control (버전 관리)

https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white

https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white

### AI & Machine Learning (인공지능 및 머신러닝)

https://img.shields.io/badge/OpenAi-412991?style=for-the-badge&logo=openai&logoColor=white

https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white

### Web Development (웹 개발)
