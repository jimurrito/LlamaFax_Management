from lib.MongoDB import MongoDB, Queue, UAuth
import streamlit as st
import os

# Site State Configuration
st.set_page_config(
    page_title="⭐🦙 Dashboard",
    page_icon="🦙",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": None,
    },
)

# [Vars from Enviroment]
# DB Host
DBHost = os.getenv("DBHOST", "LFXMongo")
buildV = os.getenv("BUILDVER", "0.0")

# Data Sources
RawQNam = "raw"
ChkQNam = "chunk"
RndQNam = "render"
ArchDBNam = "archive"
UAuthDBNam = "userAuth"
BugRepDBNam = "repBugs"
SupportColNam = "support"
TweetDBNam = "TweetBot"

RawQ = Queue(RawQNam, Host=DBHost)
ChkQ = Queue(ChkQNam, Host=DBHost)
RndQ = Queue(RndQNam, Host=DBHost)

ArchiveDB = MongoDB(ArchDBNam, Indexes="raw", Host=DBHost)
UAuthDB = UAuth(UAuthDBNam, Host=DBHost)
BugRepDB = MongoDB(BugRepDBNam, Host=DBHost)
SupportDB = MongoDB(SupportColNam, DBHost, Indexes="SrID#")
TwtHistDB = MongoDB("history", DBHost, TweetDBNam)


st.header("Dashboard")

with st.form("Main",True):
    st.write("**Administration**")
    col1, col2, col3 = st.columns(3)
    # 1st Row
    col1.subheader("Users")
    col1.write(f"#### {UAuthDB.count()}")
    col2.subheader("Bug Report")
    col2.write(f"#### {BugRepDB.count()}")
    col3.subheader("Support Tickets")
    col3.write(f"#### {SupportDB.count()}")
    "***"
    st.write("**Llamafax Core**")
    st.write("> Queues")
    col1, col2, col3 = st.columns(3)
    col1.subheader("Raw")
    col1.write(f"#### {RawQ.count()}")
    col2.subheader("Chunk")
    col2.write(f"#### {ChkQ.count()}")
    col3.subheader("Render")
    col3.write(f"#### {RndQ.count()}")
    st.write("> Databases")
    col1, col2, col3 = st.columns(3)
    col1.subheader("Rated Sets")
    col1.write(f"#### {ArchiveDB.count()}")
    col2.subheader("Twitter Posts")
    col2.write(f"#### {TwtHistDB.count()}")
    "***"


    st.form_submit_button("↻ Refresh")









st.write(f"Build v{buildV}")
