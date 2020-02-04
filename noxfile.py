import nox


@nox.session(python=["2.7", "3.4", "3.5", "3.6", "3.7", "3.8", "pypy", "pypy3"])
def tests(session):
    session.log("============ TESTS ============")
    session.run("python", "--version")


@nox.session
def lint(session):
    session.log("============ LINT ============")
    session.run("python", "--version")


@nox.session(python="3.8")
def docs(session):
    session.log("============ DOCS ============")
    session.run("python", "--version")
