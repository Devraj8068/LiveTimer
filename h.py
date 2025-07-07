import streamlit as st
from datetime import datetime
import pytz
import time

# --- Page config ---
st.set_page_config(page_title="Live Digital Clock", page_icon="🕰️", layout="centered")
st.title("🕰️ Live Digital Clock")

# --- Timezone selector ---
timezones = [
    # Asia
    "Asia/Kolkata", "Asia/Tokyo", "Asia/Shanghai", "Asia/Dubai", "Asia/Singapore",
    "Asia/Hong_Kong", "Asia/Seoul", "Asia/Bangkok", "Asia/Jakarta", "Asia/Manila",
    "Asia/Kuala_Lumpur", "Asia/Karachi", "Asia/Dhaka", "Asia/Riyadh", "Asia/Tehran",
    "Asia/Kabul", "Asia/Tashkent", "Asia/Almaty", "Asia/Yerevan", "Asia/Baku",
    
    # Europe
    "Europe/London", "Europe/Berlin", "Europe/Paris", "Europe/Rome", "Europe/Madrid",
    "Europe/Amsterdam", "Europe/Vienna", "Europe/Prague", "Europe/Warsaw", "Europe/Budapest",
    "Europe/Stockholm", "Europe/Oslo", "Europe/Copenhagen", "Europe/Helsinki", "Europe/Athens",
    "Europe/Moscow", "Europe/Istanbul", "Europe/Zurich", "Europe/Brussels", "Europe/Dublin",
    
    # North America
    "US/Eastern", "US/Central", "US/Mountain", "US/Pacific", "US/Alaska", "US/Hawaii",
    "Canada/Eastern", "Canada/Central", "Canada/Mountain", "Canada/Pacific",
    "America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles",
    "America/Toronto", "America/Vancouver", "America/Mexico_City", "America/Havana",
    
    # South America
    "America/Sao_Paulo", "America/Buenos_Aires", "America/Lima", "America/Bogota",
    "America/Santiago", "America/Caracas", "America/La_Paz", "America/Montevideo",
    
    # Africa
    "Africa/Cairo", "Africa/Lagos", "Africa/Johannesburg", "Africa/Nairobi", "Africa/Casablanca",
    "Africa/Algiers", "Africa/Tunis", "Africa/Accra", "Africa/Kinshasa", "Africa/Addis_Ababa",
    
    # Australia & Oceania
    "Australia/Sydney", "Australia/Melbourne", "Australia/Brisbane", "Australia/Perth",
    "Australia/Adelaide", "Australia/Darwin", "Pacific/Auckland", "Pacific/Fiji",
    "Pacific/Honolulu", "Pacific/Guam", "Pacific/Tahiti",
    
    # Others
    "UTC", "GMT", "Antarctica/McMurdo"
]

selected_zone = st.selectbox("🌍 Choose Time Zone:", timezones)

# --- Time format selector ---
time_formats = ["12 Hour", "24 Hour"]
selected_format = st.selectbox("🕐 Choose Time Format:", time_formats)

# --- Show time button ---
show_time_button = st.button("🕒 Start Current Date and Time")

# --- Live time display ---
if show_time_button:
    # Create placeholders for live updates
    time_placeholder = st.empty()
    date_placeholder = st.empty()
    
    # Live update loop
    while True:
        tz = pytz.timezone(selected_zone)
        now = datetime.now(tz)
        
        # Format time based on selection
        if selected_format == "12 Hour":
            time_str = now.strftime("%I:%M:%S %p")
        else:  # 24 Hour
            time_str = now.strftime("%H:%M:%S")
        
        date_str = now.strftime("%A, %d %B %Y")
        
        # Update the display
        with time_placeholder.container():
            st.success(f"🕒 Live Time in `{selected_zone}`: {time_str}")
        
        with date_placeholder.container():
            st.info(f"📅 Date: {date_str}")
        
        # Wait 1 second before updating again
        time.sleep(1)

# --- Instructions ---
st.markdown("---")
st.markdown("**💡 How to use:**")
st.markdown("1. Select your desired timezone from the dropdown")
st.markdown("2. Choose your preferred time format (12 Hour or 24 Hour)")
st.markdown("3. Click the 'Start Live Clock' button to begin live time display")
st.markdown("4. The time will update every second automatically")
st.markdown("5. To change timezone or format, refresh the page")

st.markdown("**🌍 Features:**")
st.markdown("- **Multiple timezones**: Choose from 70+ different time zones worldwide")
st.markdown("- **Time format options**: 12-hour (with AM/PM) or 24-hour format")
st.markdown("- **Live updates**: Time updates every second automatically")
st.markdown("- **Complete information**: Shows both time and date")
st.markdown("- **Real-time display**: Live clock")