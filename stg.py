import speedtest
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Internet Speed Test")

# Create the download speed label
download_speed_label = tk.Label(root, text="Download Speed")
download_speed_label.pack()

# Create the upload speed label
upload_speed_label = tk.Label(root, text="Upload Speed")
upload_speed_label.pack()

# Create the download speed graph
download_speed_graph = tk.Canvas(root, width=200, height=100)
download_speed_graph.pack()

# Create the upload speed graph
upload_speed_graph = tk.Canvas(root, width=200, height=100)
upload_speed_graph.pack()

# Create the start button
def start_speed_test():
  # Get the download and upload speed
  download_speed = speedtest.Speedtest().download()
  upload_speed = speedtest.Speedtest().upload()

  # Update the labels with the speed
  download_speed_label.config(text="Download Speed: {} Mb/s".format(round(download_speed / (2 ** 20))))
  upload_speed_label.config(text="Upload Speed: {} Mb/s".format(round(upload_speed / (2 ** 20))))

  # Update the graphs with the speed
  download_speed_graph.create_line(0, 0, 200, download_speed, fill="blue")
  upload_speed_graph.create_line(0, 0, 200, upload_speed, fill="red")

# Create the start button
start_button = tk.Button(root, text="Start", command=start_speed_test)
start_button.pack()

# Start the main loop
root.mainloop()
