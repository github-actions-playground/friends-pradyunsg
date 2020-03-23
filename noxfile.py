import nox


@nox.session
def primary(session):
    session.log("============ PRIMARY ============")
    session.run("python", "--version")


@nox.session
def secondary(session):
    session.log("============ SECONDARY ============")
    session.run("python", "--version")


@nox.session(python="3.8")
def experimental(session):
    session.log("============ EXPERIMENTAL ============")
    session.run("python", "--version")
    session.error("This should always fail")
