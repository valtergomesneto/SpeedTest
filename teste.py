import speedtest

st = speedtest.Speedtest()

velocidadeDownload = st.download()/1024/1024
velocidadeUpload = st.upload()/1024/1024

download_formatado = "{:.2f}".format(velocidadeDownload)
upload_formatado = "{:.2f}".format(velocidadeUpload)


print("Download: " + download_formatado + "Mbps")
print("Upload: " + upload_formatado + "Mbps")