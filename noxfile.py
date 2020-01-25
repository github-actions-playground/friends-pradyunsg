import nox


@nox.session(python=["2.7", "3.4", "3.5", "3.6", "3.7", "3.8"])
def tests(session):
    session.log("This is tests on...")
    session.run("python", "--version")


@nox.session
def lint(session):
    session.log("This is lint on...")
    session.run("python", "--version")


@nox.session(python="3.8")
def docs(session):
    session.log("This is docs on...")
    session.run("python", "--version")
