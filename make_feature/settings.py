import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IDA_DIR = os.path.join(os.path.dirname(BASE_DIR),'ida')

# acs 저장 경로
ACS_PATH = os.path.join(BASE_DIR,'./acs')
# fh_acs 저장 경로
FH_ACS_PATH = os.path.join(BASE_DIR,'./fh_acs')

# fops 저장 경로
FOPS_PATH = os.path.join(IDA_DIR,'./fops')
# fh_fops 저장 경로
FH_FOPS_PATH = os.path.join(BASE_DIR,'./fh_fops')

# CPU COUNT
CPU_COUNT = 4

# Feature Hashing 관련 상수 정의
# 최대 리스트 크기 ( 2 ^ k )
FEATURE_VECTOR_K = 12

MAX_LIST_SIZE = 1 << FEATURE_VECTOR_K
MOD_VALUE = ( 1 << (FEATURE_VECTOR_K  + 1) ) -  1


# n-gram 시작
N_GRAM_START = 3

# n-gram 끝
N_GRAM_END = 5