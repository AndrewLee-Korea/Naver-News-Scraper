# Analysis of Naver News — Scraping, NLP Preprocessing, and LDA Topic Modeling

A Python-based pipeline for scraping Korean news articles from Naver and performing topic modeling analysis using LDA.

**[한국어 버전은 아래에 있습니다](#한국어)**

---

## Overview

This project provides an end-to-end solution for Korean news text analysis:

1. **Scraping**: Collect news articles from Naver News based on search keywords
2. **Analysis**: Perform text preprocessing, morphological analysis, and LDA topic modeling

## Features

- Automated news article scraping with pagination support
- Korean morphological analysis using Komoran
- TF-IDF vectorization and word frequency analysis
- LDA topic modeling with coherence score optimization
- Interactive visualization with pyLDAvis and Word Cloud

## Project Structure

```
Naver-News-Scraper/
├── scrape_naver_news.ipynb    # News scraping notebook
├── analyze_naver_news.ipynb   # Topic modeling notebook
├── get_naver_news.py          # Scraping utility functions
├── morphemeAnalysis2.py       # Text preprocessing functions
├── data/                      # Scraped data storage
└── result/                    # Analysis output (HTML, images)
```

## Requirements

```
python >= 3.7
selenium
webdriver-manager
beautifulsoup4
requests
pandas
numpy
konlpy
gensim
pyLDAvis
scikit-learn
matplotlib
seaborn
wordcloud
```

## Installation

```bash
# Clone the repository
git clone https://github.com/AndrewLee-Korea/Naver-News-Scraper.git
cd Naver-News-Scraper

# Install dependencies
pip install -r requirements.txt

# Install KoNLPy (requires Java)
pip install konlpy
```

> **Note**: KoNLPy requires Java Runtime Environment (JRE). Please ensure Java is installed on your system.

## Usage

### Step 1: Scrape News Articles

Open `scrape_naver_news.ipynb` and configure the following parameters:

```python
# Set search keyword
search = '치매'  # Example: "dementia"

# Set page range (each page contains 10 articles)
page = 1      # Start page
page2 = 100   # End page
```

Run all cells to scrape articles. The output will be saved as a DataFrame with columns: `title`, `link`, `content`.

### Step 2: Analyze with Topic Modeling

Open `analyze_naver_news.ipynb` and run the analysis pipeline:

1. **Preprocessing**: Load data and extract nouns using Komoran
2. **Feature Engineering**: Configure max features for analysis
3. **Word Cloud**: Visualize frequent terms
4. **TF-IDF Analysis**: Identify important terms
5. **LDA Modeling**: Discover latent topics
6. **Visualization**: Generate interactive pyLDAvis output

Key parameters to adjust:

```python
my_max_feature = 30      # Number of features
num_topics = 5           # Number of topics for LDA
passes = 20              # Training iterations
```

## Output

- **Word Cloud**: Visual representation of term frequency
- **LDA Visualization**: Interactive HTML file via pyLDAvis
- **Coherence Scores**: Model quality metrics (c_v, UMass)

## License

This project is licensed under the MIT License.

## Author

Andrew Lee ([@AndrewLee-Korea](https://github.com/AndrewLee-Korea))

---

<a name="한국어"></a>
# 네이버 뉴스 분석 — 스크래핑, NLP 전처리, LDA 토픽 모델링

네이버 뉴스 기사를 수집하고 LDA 토픽 모델링을 수행하는 Python 기반 파이프라인입니다.

---

## 개요

이 프로젝트는 한국어 뉴스 텍스트 분석을 위한 End-to-End 솔루션을 제공합니다:

1. **스크래핑**: 검색 키워드 기반 네이버 뉴스 기사 수집
2. **분석**: 텍스트 전처리, 형태소 분석, LDA 토픽 모델링 수행

## 주요 기능

- 페이지네이션을 지원하는 자동화된 뉴스 기사 스크래핑
- Komoran을 활용한 한국어 형태소 분석
- TF-IDF 벡터화 및 단어 빈도 분석
- Coherence Score 최적화를 통한 LDA 토픽 모델링
- pyLDAvis 및 Word Cloud를 활용한 인터랙티브 시각화

## 프로젝트 구조

```
Naver-News-Scraper/
├── scrape_naver_news.ipynb    # 뉴스 스크래핑 노트북
├── analyze_naver_news.ipynb   # 토픽 모델링 노트북
├── get_naver_news.py          # 스크래핑 유틸리티 함수
├── morphemeAnalysis2.py       # 텍스트 전처리 함수
├── data/                      # 수집된 데이터 저장소
└── result/                    # 분석 결과물 (HTML, 이미지)
```

## 요구사항

```
python >= 3.7
selenium
webdriver-manager
beautifulsoup4
requests
pandas
numpy
konlpy
gensim
pyLDAvis
scikit-learn
matplotlib
seaborn
wordcloud
```

## 설치 방법

```bash
# 저장소 클론
git clone https://github.com/AndrewLee-Korea/Naver-News-Scraper.git
cd Naver-News-Scraper

# 의존성 설치
pip install -r requirements.txt

# KoNLPy 설치 (Java 필요)
pip install konlpy
```

> **참고**: KoNLPy는 Java Runtime Environment (JRE)가 필요합니다. 시스템에 Java가 설치되어 있는지 확인하세요.

## 사용 방법

### Step 1: 뉴스 기사 스크래핑

`scrape_naver_news.ipynb`를 열고 다음 파라미터를 설정합니다:

```python
# 검색 키워드 설정
search = '치매'  # 예시: "치매"

# 페이지 범위 설정 (페이지당 10개 기사)
page = 1      # 시작 페이지
page2 = 100   # 종료 페이지
```

모든 셀을 실행하면 기사가 수집됩니다. 결과는 `title`, `link`, `content` 컬럼을 가진 DataFrame으로 저장됩니다.

### Step 2: 토픽 모델링 분석

`analyze_naver_news.ipynb`를 열고 분석 파이프라인을 실행합니다:

1. **전처리**: 데이터 로드 및 Komoran을 사용한 명사 추출
2. **피처 엔지니어링**: 분석용 최대 피처 수 설정
3. **Word Cloud**: 빈출 단어 시각화
4. **TF-IDF 분석**: 주요 단어 식별
5. **LDA 모델링**: 잠재 토픽 발견
6. **시각화**: pyLDAvis 인터랙티브 결과물 생성

주요 조정 파라미터:

```python
my_max_feature = 30      # 피처 수
num_topics = 5           # LDA 토픽 수
passes = 20              # 학습 반복 횟수
```

## 출력물

- **Word Cloud**: 단어 빈도의 시각적 표현
- **LDA 시각화**: pyLDAvis를 통한 인터랙티브 HTML 파일
- **Coherence Scores**: 모델 품질 지표 (c_v, UMass)

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 저자

Andrew Lee ([@AndrewLee-Korea](https://github.com/AndrewLee-Korea))
