from lib.MongoDB import MongoDB,UAuth
import streamlit as st
import os

# Site State Configuration
st.set_page_config(
    page_title="⭐🦙 Search",
    page_icon="🦙",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": None,
    },
)

DBHost = os.getenv("DBHOST", "LFXMongo")
buildV = os.getenv("BUILDVER", "0.0")

# DB Object Creation
ArchDBNam = "archive"
UAuthDBNam = "userAuth"
KeyColNam = "alphaKey"
BugRepDBNam = "repBugs"
SupportColNam = "support"
TweetDBNam = "TweetBot"

ArchiveDB = MongoDB(ArchDBNam, Indexes="raw", Host=DBHost)
UAuthDB = UAuth(UAuthDBNam, Host=DBHost)
keyDB = MongoDB(KeyColNam, DBHost, Indexes=["code"])
BugRepDB = MongoDB(BugRepDBNam, Host=DBHost, Indexes="BugID#")
SupportDB = MongoDB(SupportColNam, DBHost, Indexes="SrID#")
TwtHistDB = MongoDB("history", DBHost, TweetDBNam)


st.header("Search")


with st.form("Query,False"):
    col1, col2 = st.columns(2)

    DBType = col1.selectbox(
        "Database *",
        [
            "(Select One)",
            "Archive",
            "Alpha-keys",
            "UserAuth",
            "Bug-Report",
            "Support",
            "TweetHist",
        ],
    )
    Attribute = col2.selectbox(
        "Attribute *", ["(Select One)", "upn","use", "raw", "code", "BugID#", "SrID#", "tweet", "State"]
    )
    RetLimit = col2.number_input("Return Limit | 0 == all", min_value=0, max_value=100)
    Query = st.text_area("Query")

    st.form_submit_button("🔍")



# Map Query
if Query:
    InjectQuery = {Attribute: {"$exists": "true", "$in": [Query]}}
else:
    InjectQuery = {}

Out = False

# Input Mapping, maps DB Object based on Input type
if DBType == "Archive":
    Out = ArchiveDB.Col.find(InjectQuery)
elif DBType == "Alpha-keys":
    Out = keyDB.Col.find(InjectQuery)
elif DBType == "UserAuth":
    Out = UAuthDB.Col.find(InjectQuery)
elif DBType == "Bug-Report":
    Out = BugRepDB.Col.find(InjectQuery)
elif DBType == "Support":
    Out = SupportDB.Col.find(InjectQuery)
elif DBType == "TweetHist":
    Out = TwtHistDB.Col.find(InjectQuery)

if Out:
    ct = 0
    # Sanitize and write output
    for Result in list(Out):        
        if ct == RetLimit != 0:
            break
        try:
            Result.pop("_id")
            Result.pop("pwd")
        except:
            pass
        st.write(Result)
        ct += 1


st.write(f"Build v{buildV}")