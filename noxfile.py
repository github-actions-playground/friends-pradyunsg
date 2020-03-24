import nox


@nox.session(python=False)
def primary(session):
    session.log("============ PRIMARY ============")
    session.run("python", "--version")


@nox.session(python=False)
def secondary(session):
    session.log("============ SECONDARY ============")
    session.run("python", "--version")


@nox.session(python=False)
def experimental(session):
    session.log("============ EXPERIMENTAL ============")
    session.run("python", "--version")
    session.error("This should always fail")
