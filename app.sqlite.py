# same program using sqlite3 database
import sqlite3 
conn=sqlite3.connect("sqlite_database.txt")
cursor=conn.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS youtube(
               id  INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               status TEXT NOT NULL
        )
''')



def list_all_the_videos():
    cursor.execute("SELECT * FROM youtube")
    print("\n")
    print("*"*80)
    for video in cursor.fetchall():
        print(video)
    print("*"*80)
    print("\n")
    conn.commit()

def add_the_video():
    user_input_name=input("Enter the video name:\t")
    user_input_status=input("Enter video status watched || not watched:\t")
    cursor.execute("INSERT INTO youtube (name,status) VALUES (?,?)",(user_input_name,user_input_status))
    conn.commit()

def delete_the_video():
    index=int(input("Enter the index of video to be deleted"))
    cursor.execute("DELETE FROM youtube WHERE id=?",(index,))
    conn.commit()

def update_the_video():
    index=int(input("Enter the index of video to be updated"))
    new_video_name=input("Enter the new video name")
    new_video_status=input("Enter the new video status")
    cursor.execute("UPDATE youtube SET name=?, status=? WHERE id=?",(new_video_name,new_video_status,index))
    conn.commit()

def search_the_video():
    search_video_name = input("Enter the name of the video you want to search: ")
    cursor.execute("SELECT * FROM youtube WHERE name=?", (search_video_name,))
    result = cursor.fetchall()
    if result:
        print("Search Result:")
        print(result)
    else:
        print("No video found with that name.")
    conn.commit()

def main():
    while True:
        print("YOUTUBE MANAGER APP || HOME FOR THE DEVELOPER\n")
        print("1.List all the videos:\t")
        print("2.Add the videos:\t")
        print("3.Update the video:\t")
        print("4.Delete the video:\t")
        print("5. Search the video:\t")
        print("6.Exit the program\n")

        choice=int(input("Enter the your choice.."))

        if choice==1:
            print("You are in list all the video section..")
            list_all_the_videos()
        elif choice==2:
            print("You are in add video section")
            add_the_video()
        elif choice==3:
            print("You are in update video section..")
            update_the_video()
        elif choice==4:
            print("you are in delete video section")
            delete_the_video()
        elif choice==5:
            print("you are in search video section..")
            search_the_video()
        elif choice==6:
            conn.close()
            exit()
        else:
            print("Invalid user input")
        

if __name__=="__main__":
    main()