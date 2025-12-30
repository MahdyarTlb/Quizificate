from project import load_questions, run_quiz, generate_certificate, main
import project

def test_load_questions():

    questions = load_questions()

    assert isinstance(questions, list)

def test_run_quiz():
    result = run_quiz([])

    assert isinstance(result, tuple)
    assert result == (0,0)

def test_certificate():

    assert generate_certificate("Ali", 10, 5) is False

    assert generate_certificate("mmad", 70, 7) is True

    assert generate_certificate("", 10, 5) is False

def test_main(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "Ali")

    monkeypatch.setattr(project, "load_questions", lambda: [])
    monkeypatch.setattr(project, "run_quiz", lambda q: (0, 0))

    monkeypatch.setattr(
        project,
        "generate_certificate",
        lambda name, score, total: True
    )

    main()