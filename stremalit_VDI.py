import streamlit as st
# import pandas as pd
# import altair as alt
# import pyodbc


st.write('dddddd')
# server = 'verticaldynamix.database.windows.net'
# database = 'VerticalDynamix'
# username = 'VerticalDynamix'
# password = 'Golemw#153'
# driver = '{ODBC Driver 17 for SQL Server}'
# connection_string = f"Driver={driver};Server={server};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

# try:
#     conn = pyodbc.connect(connection_string)
#     st.success("Connected to the database successfully!")

#     st.title("TB Units Per Day Report")

#     st.markdown(
#     """
#     <style>
#     div[data-testid="stDateInput"] {
#         background-color: #222;  /* Dark background */
#         border: 1px solid #aaa;  /* Border color */
#         border-radius: 5px;
#         padding: 5px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
#     )

#     # Date selection widgets
#     from_date = st.date_input("Select From Date")
#     to_date = st.date_input("Select To Date")

#     from_date = from_date.strftime('%Y-%m-%d')
#     to_date = to_date.strftime('%Y-%m-%d')

#     if from_date and to_date:
#         if from_date > to_date:
#             st.error("From date must be before To date.")
#         else:
#             sql_query = '''
#             SELECT LCP_name, TB_units, startDate, UserName
#             FROM DataTimeBucketPB
#             WHERE startDate BETWEEN ? AND ?
            
#             '''
#             df = pd.read_sql(sql_query, conn, params=(from_date, to_date))
        
#             # Close the connection
#             conn.close()

#             # # Execute the query and fetch data
#             # cursor = conn.cursor()
#             # cursor.execute(sql_query, (from_date, to_date))
#             # data = cursor.fetchall()

#             # columns = ['LCP_name', 'TB_units', 'startDate', 'UserName']
#             # df = pd.DataFrame(data, columns=columns)

            
#             # st.write(df)
#             # df = pd.DataFrame(data, columns=['LCP_name', 'TB_units', 'startDate', 'UserName'])
#             # # df = pd.DataFrame(data)
#             # st.write(df)

#             if not df.empty:
#                 df['startDate'] = pd.to_datetime(df['startDate'])

#                 ### per LCP
#                 df_LCP = df.groupby('LCP_name')['TB_units'].sum().reset_index()
#                 df_LCP.columns = ['LCP', 'TB_Units']

#                 st.write("Grouped Data:")
#                 st.write(df_LCP)

#                 # Ensure TB_units is numeric
#                 df['TB_units'] = pd.to_numeric(df['TB_units'], errors='coerce')

#                 # Check for null or NaN values after conversion
#                 st.write("Null values in TB_units after conversion:", df['TB_units'].isnull().sum())

#                 base_chartLCP = (
#                     alt.Chart(df_LCP)
#                     .mark_bar(width=30, color='rgb(225, 194, 51)')  # Adjust bar width and color
#                     .encode(
#                         y=alt.Y('LCP:N', title='LCP', sort='-x'),  # Move the categorical text column to the y-axis
#                         x=alt.X('TB_Units:Q', title='TB_Units'),
#                     )
#                     .properties(width=700, height=400)  # Adjust chart dimensions
#                 )

               
#                 text = base_chartLCP.mark_text(
#                     align='left',
#                     baseline='middle',
#                     dy=-5,  # Offset for the text
#                     color='rgb(255, 255, 255)'
#                 ).encode(
#                     text='TB_Units:Q'
#                 )

#                 # Combine chart and text into a LayerChart
#                 layered_chartLCP = alt.layer(base_chartLCP, text).configure_axis(
#                     labelFontSize=12,
#                     titleFontSize=14
#                 )

#                 # Display the chart in Streamlit
#                 # st.altair_chart(layered_chartLCP, use_container_width=True)

#                 ### end per LCP
#                 #### chart per day
#                 daily_tb_units = df.groupby(df['startDate'].dt.date)['TB_units'].sum().reset_index()
#                 daily_tb_units.columns = ['Date', 'Total TB Units']

#                 # Create a bar chart with Altair
#                 base_chart = (
#                     alt.Chart(daily_tb_units)
#                     .mark_bar(width=30, color='rgb(225, 194, 51)')  # Adjust bar width and color
#                     .encode(
#                         x=alt.X('Date:T', title='Date'),
#                         y=alt.Y('Total TB Units:Q', title='Total TB Units'),
#                     )
#                     .properties(width=700, height=400)  # Adjust chart dimensions
#                 )

#                 # Add text labels on top of the bars
#                 text = base_chart.mark_text(
#                     align='center',
#                     baseline='bottom',
#                     dy=-5,  # Offset for the text
#                     color='rgb(255, 255, 255)'
#                 ).encode(
#                     text='Total TB Units:Q'
#                 )

#                 # Combine chart and text into a LayerChart
#                 layered_chart = alt.layer(base_chart, text).configure_axis(
#                     labelFontSize=12,
#                     titleFontSize=14
#                 )

#                 col1, col2 = st.columns([1, 1])
#                 # Display the chart in Streamlit
#                 with col1:
#                     st.altair_chart(layered_chart, use_container_width=True)
#                 with col2:
#                     st.altair_chart(layered_chartLCP, use_container_width=True)
#             else:
#                 st.warning("No data found for the selected date range.")
# # nova promena
# except Exception as e:
#     st.error(f"An error occurred: {e}")