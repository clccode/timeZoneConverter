import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Time Zone Converter", page_icon="🕰️")

st.title("🕰️ Time Zone Converter")

# get user input for time and time zone
selected_date = st.date_input("Select the date")
selected_time = st.time_input("Select a time")

# combine date and time into a datetime object
dt = datetime.combine(selected_date, selected_time)

# get user input for source and target time zones
from_tz = st.selectbox("From Time Zone", pytz.all_timezones,index=pytz.all_timezones.index("UTC"))
to_tz = st.selectbox("To Time Zone", pytz.all_timezones, index=pytz.all_timezones.index("Asia/Tokyo"))

# convert button
if st.button("Convert"):
    try:
        # combine date and time
        naive_dt = datetime.combine(selected_date, selected_time)

        # define time zones
        from_zone = pytz.timezone(from_tz)
        to_zone = pytz.timezone(to_tz)

        # localize and convert the datetime
        localized_dt = from_zone.localize(naive_dt)
        converted_dt = localized_dt.astimezone(to_zone)

        # display results
        st.success(f"🕰️ Original ({from_tz}): {localized_dt.strftime('%Y-%m-%d %H:%M:%S')}")
        st.success(f"🌎 Converted ({to_tz}): {converted_dt.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        st.error(f"Error combining date and time: {e}")