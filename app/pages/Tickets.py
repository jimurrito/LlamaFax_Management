from lib.MongoDB import MongoDB
import streamlit as st
import os

# Site State Configuration
st.set_page_config(
    page_title="⭐🦙 Tickets",
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

BugRepDBNam = "repBugs"
SupportColNam = "support"

BugRepDB = MongoDB(BugRepDBNam, Host=DBHost)
SupportDB = MongoDB(SupportColNam, DBHost, Indexes="SrID#")


st.header("Ticket Manager")
"***"
"#### Categories"
""
col1, col2 = st.columns(2)
BgRp = col1.button("Bug-Reports")
SupT = col2.button("Support-Tickets")

"***"

if BgRp:
    with st.container():

        Results = list(BugRepDB.Col.find())

        if not Results:
            st.write("No Results Found 🐼")

        else:

            for Report in BugRepDB.Col.find():

                if Report["State"] == "Open":
                    Emoji = "🔴"
                else:
                    Emoji = "🟢"
                with st.expander(
                    f"{Emoji} [ {Report['State']} ] | BugID#: {Report['BugID#']} | User: {Report['SubUsr']}"
                ):
                    st.write(Report)


elif SupT:
    with st.container():

        Results = list(SupportDB.Col.find())

        if not Results:
            st.write("No Results Found 🐼")

        else:

            for Report in SupportDB.Col.find():

                if Report["State"] == "Open":
                    Emoji = "🔴"
                else:
                    Emoji = "🟢"
                with st.expander(
                    f"{Emoji} [ {Report['State']} ] | BugID#: {Report['BugID#']} | User: {Report['SubUsr']}"
                ):
                    st.write(Report)

""
st.write(f"Build v{buildV}")
