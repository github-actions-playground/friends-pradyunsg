import os
import nox


@nox.session(python=False)
def primary(session):
    session.log("============ PRIMARY ============")
    session.run("python", "--version")
    session.log(os.environ)
