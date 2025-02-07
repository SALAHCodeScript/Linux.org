import sys
import rich

shows = ["Serie", "Anime", "Movie"]
show = sys.argv[1] if sys.argv[1].capitalize() in shows else sys.exit()

data_path = f"/home/mint/Documents/.watching/{sys.argv[1].lower()}"

def showNames(data):
    with open(data, 'r') as file:
        content_line = ""
        content_data = []
        for line in file.readlines():
            for char in line:
                if char == "\t":
                    break
                content_line += char
            content_data.append(content_line)
            content_line = ""
        file.close()
    return content_data

def showEpisodes(data):
    with open(data, 'r') as file:
        content_line = ""
        content_data = []
        for line in file.readlines():
            for char in line:
                if char == "/" and line[line.find('/')+1].isdigit():
                    episode = line[line.find('/')-5:line.find('/')] + line[line.find('/'):line.find('\n')]
                    episode = episode[episode.find('\t', episode.count('\t')-1)+1:] if not('\t' in line[line.find('/'):line.find('\n')]) else episode[:episode.find('/')].replace('\t', '') + episode[episode.find('/'):episode.find('\n')].replace('\t', ' ')
                    content_line += episode
            content_data.append(content_line)
            content_line = ""
        file.close()
    return content_data

def buildShow(names, episodes):
    dict_data = {}
    if len(names) == len(episodes):
        for name in range(len(names)):
            dict_data[names[name]] = episodes[name]
    return dict_data

def displayData():
    data = buildShow(showNames(data_path), showEpisodes(data_path))
    rich.print(data)

try:
    if sys.argv[2] == "display":
        if sys.argv[3] == "names":
            rich.print(showNames(data_path))
        elif sys.argv[3] == "episode" and sys.argv[4] != "":
            user_show = sys.argv[4]
            for show in showNames(data_path):
                if user_show.title() in show:
                    user_show = show
                elif user_show.lower() in show:
                    user_show = show
            index = showNames(data_path).index(user_show)
            rich.print(showEpisodes(data_path)[index])
        else:
            displayData()
except IndexError:
    print(f"what do want from this '{show} show' to do for you?")


