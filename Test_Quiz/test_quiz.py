from quiz import load_questions, run_quiz

def test_load_questions():

    questions = load_questions()

    assert isinstance(questions, list)

def test_run_quiz():
    result = run_quiz([])

    assert isinstance(result, tuple)
    assert result == (0,0)