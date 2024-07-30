import threading

# Define a function to process a chunk of data
def process_chunk(chunk):
    # Process the chunk here
    print(f"Processing chunk: {chunk}")

# Define the main function to divide the task into chunks and process them using threads
def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Sample data
    chunk_size = 3  # Define the size of each chunk

    threads = []  # List to store the thread objects

    # Divide the data into chunks and create a thread for each chunk
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        thread = threading.Thread(target=process_chunk, args=(chunk,))
        threads.append(thread)

    # Start all the threads
    for thread in threads:
        thread.start()

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
