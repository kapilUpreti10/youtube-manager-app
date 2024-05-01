import json 
fileName = "dataFile.txt"
def fetch_data():
    try:
        with open (fileName,"r") as file:
            data =json.load(file)
            return data
    except FileNotFoundError:
        data=[]
        return data

def  save_data_helper(videos):
    with open(fileName,"w") as file:
        json.dump(videos,file)

def list_all_videos(videos):
    for index,video in enumerate(videos):
        print(f"{index+1}. {video}")

def add_video(videos):
    video=input("Enter the video name: ")
    status=input("Enter the status of the video:: watched || not watched: ")
    videos.appned({'video':video,'status':'not watched'})
    save_data_helper(videos)

def delete_video(videos):
    pass

def update_video(videos):
    pass

def search_video(videos):
    pass


def main():
    videos = fetch_data()
    while True:
        print("\n\nYOUTUBE MANAGER APP || HOME FOR THE DEVELOPER\n")
        print("1.List all the videos")
        print("2.Add a video")
        print("3.Delete a video")
        print("4.Update a video")
        print("5.Search a video")
        print("6.Exit\n")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                print("Listing all the videos....")
                list_all_videos(videos)
                break
                
            case 2:
                print("Adding a video....")
                add_video(videos)
                break
            case 3:
                print("Deleting a video....")
                delete_video(videos)
                break
            case 4:
                print("Updating a video....")
                update_video(videos)
                break
            case 5:
                print("Searching a video....")
                search_video(videos)
                break
            case 6:
                print("Exiting the app....")
                exit()
            case _:
                print("Enter a valid choice....")
                break

if __name__ == "__main__":
    main()
