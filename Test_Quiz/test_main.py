import main
import quiz, certificate

def test_main(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "Ali")

    monkeypatch.setattr(quiz, "load_questions", lambda: [])
    monkeypatch.setattr(quiz, "run_quiz", lambda q: (0, 0))

    monkeypatch.setattr(
        certificate,
        "generate_certificate",
        lambda name, score, total: True
    )

    main.main()