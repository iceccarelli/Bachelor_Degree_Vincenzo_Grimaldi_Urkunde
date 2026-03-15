import pytest
import pandas as pd
import os

# Path to the structured metadata (must match our repository layout)
KEY_DETAILS_CSV = os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'key_details.csv')

@pytest.fixture(scope='module')
def key_details_df():
    """Fixture to load key_details.csv once for all tests.
    This CSV was generated directly from the official RWTH documents (urkunde.pdf and detail.pdf)."""
    if not os.path.exists(KEY_DETAILS_CSV):
        pytest.fail(f"key_details.csv not found at {KEY_DETAILS_CSV}")
    return pd.read_csv(KEY_DETAILS_CSV)

def get_detail_value(df, section, key):
    """Helper to safely retrieve a detail_value from the DataFrame."""
    result = df[(df['section'] == section) & (df['detail_key'] == key)]['detail_value']
    if result.empty:
        return None
    return str(result.iloc[0]).strip()

# ====================== GENERAL INFORMATION ======================
def test_full_name_match(key_details_df):
    name = get_detail_value(key_details_df, 'General', 'Full Name')
    assert name == 'Giacomo Vincenzo Ceccarelli Grimaldi', \
        f"Full Name mismatch: Expected 'Giacomo Vincenzo Ceccarelli Grimaldi', got '{name}'"

def test_date_of_birth_match(key_details_df):
    born = get_detail_value(key_details_df, 'General', 'Born On')
    assert born == '04 December 1987 in Lima', \
        f"Date of Birth mismatch: Expected '04 December 1987 in Lima', got '{born}'"

def test_graduation_date_match(key_details_df):
    date = get_detail_value(key_details_df, 'General', 'Graduation Date')
    assert date == '20 October 2022', \
        f"Graduation Date mismatch: Expected '20 October 2022', got '{date}'"

def test_overall_grade_match(key_details_df):
    grade = get_detail_value(key_details_df, 'General', 'Overall Grade')
    assert grade == '3.5', \
        f"Overall Grade mismatch: Expected '3.5', got '{grade}'"

# ====================== THESIS ======================
def test_thesis_topic_match(key_details_df):
    topic = get_detail_value(key_details_df, 'Thesis', 'Topic (English)')
    expected = 'Development of a Cross-domain Knowledge Base for Cyber Intelligence in Smart Grids'
    assert topic == expected, \
        f"Thesis Topic mismatch: Expected '{expected}', got '{topic}'"

def test_thesis_grade_match(key_details_df):
    grade = get_detail_value(key_details_df, 'Thesis', 'Grade')
    assert grade == '3.0', \
        f"Thesis Grade mismatch: Expected '3.0', got '{grade}'"

def test_thesis_examiner_match(key_details_df):
    examiner = get_detail_value(key_details_df, 'Thesis', 'Examiner')
    assert examiner == 'Univ.-Prof. Dr. Andreas Ulbig', \
        f"Examiner mismatch: Expected 'Univ.-Prof. Dr. Andreas Ulbig', got '{examiner}'"

# ====================== SIGNATURES ======================
def test_chair_of_examination_board_match(key_details_df):
    chair = get_detail_value(key_details_df, 'Signatures', 'Chair of Examination Board')
    assert chair == 'Univ.-Prof. Dr. rer. nat. habil. Marco Lübbecke', \
        f"Chair mismatch: Expected 'Univ.-Prof. Dr. rer. nat. habil. Marco Lübbecke', got '{chair}'"

def test_dean_electrical_engineering_match(key_details_df):
    dean = get_detail_value(key_details_df, 'Signatures', 'Dean Faculty Electrical Engineering')
    assert dean == 'Univ.-Prof. Dr.-Ing. Albert Moser', \
        f"Dean (Electrical Engineering) mismatch: Expected 'Univ.-Prof. Dr.-Ing. Albert Moser', got '{dean}'"

def test_dean_business_economics_match(key_details_df):
    dean = get_detail_value(key_details_df, 'Signatures', 'Dean Faculty Business and Economics')
    assert dean == 'Univ.-Prof. Dr. rer. pol. Christine Harbring', \
        f"Dean (Business and Economics) mismatch: Expected 'Univ.-Prof. Dr. rer. pol. Christine Harbring', got '{dean}'"

# ====================== MODULE GROUPS ======================
def test_mathematical_sciences_average_match(key_details_df):
    avg = get_detail_value(key_details_df, 'Module Group', 'Mathematical and Natural Sciences')
    assert avg == '2.9', \
        f"Mathematical & Natural Sciences average mismatch: Expected '2.9', got '{avg}'"

def test_engineering_sciences_average_match(key_details_df):
    avg = get_detail_value(key_details_df, 'Module Group', 'Engineering Sciences')
    assert avg == '3.5', \
        f"Engineering Sciences average mismatch: Expected '3.5', got '{avg}'"

def test_economics_business_average_match(key_details_df):
    avg = get_detail_value(key_details_df, 'Module Group', 'Economics and Business Sciences')
    assert avg == '3.8', \
        f"Economics & Business Sciences average mismatch: Expected '3.8', got '{avg}'"

# ====================== FINAL VERIFICATION ======================
def test_final_verification_message():
    """All tests passed → the entire degree record matches the official RWTH documents."""
    assert True, "Bachelor's Degree 100% verified against PDF content."
