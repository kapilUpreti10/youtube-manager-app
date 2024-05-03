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
        print("Data saved successfully....")

def ask_user_to_quit_program():
    # user_input = input("Do you want to exit the program? (yes/no): ")
    # if user_input.lower() == "yes":
    #     exit()
    # else:
    #     pass
     pass

def list_all_videos(videos):
    print("*"*80)
    for index,video in enumerate(videos):
        print(f"{index+1}.  Video Name: {video['video']}  ||  Status: {video['status']}")
    print("*"*80)  
    ask_user_to_quit_program()

def add_video(videos):
    video=input("Enter the video name to be added: ")
    status=input("Enter the status of the video:: watched || not watched: ")
    videos.append({'video':video,'status':status})
    save_data_helper(videos)
    print("new videos list is:: ")
    list_all_videos(videos)
    ask_user_to_quit_program()

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to be deleted: "))
    videos.pop(index-1)
    save_data_helper(videos)
    print("new videos list is:: ")
    list_all_videos(videos)
    ask_user_to_quit_program()

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to be updated: "))
    video=input("Enter the new video name: ")
    status=input("Enter the status of the video:: watched || not watched: ")
    videos[index-1]={'video':video,'status':status}
    save_data_helper(videos)
    print("new videos list is:: ")
    list_all_videos(videos)
    ask_user_to_quit_program()

def search_video(videos):
    video_name = input("Enter the video name to be searched: ")
    for video in videos:
        if video['video'] == video_name:
            print(f"Video Name:{video['video']}  ||  Status: {video['status']}")
            break
    else:
        print("Video not found....")
    ask_user_to_quit_program()


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
                print("You are in list video section\n")
                list_all_videos(videos)
                
            case 2:
                print("You are in add video section.")
                add_video(videos)
            case 3:
                print("You are in delete video section....")
                delete_video(videos)
            case 4:
                print("You are in update video section...")
                update_video(videos)
            case 5:
                print("You are in search video section....")
                search_video(videos)
            case 6:
                print("Exiting the app....")
                exit()
            case _:
                print("Enter a valid choice....")
                break

if __name__ == "__main__":
    main()
