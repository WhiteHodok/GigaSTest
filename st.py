'''
this script was made for testing internet speed on my home server,
who know maybe ii use this script later in my petproject
'''
import speedtest

# get as short name
st = speedtest.Speedtest()

#info about download speed with round on ,xx
ds = st.download()
print(round(ds/(2**20), 2))

#info about upload speed with round on ,xx
us = st.upload()
print(round(us/(2**20), 2))
