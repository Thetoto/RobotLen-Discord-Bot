from discord import embeds


def queue_embed(queue):
    res = embeds.Embed(title="Musiques en attente", type="rich")
    np_str = "Aucune musique en cours"
    if queue.is_playing():
        np_str = queue.current.data.get('snippet').get('title')
    res.add_field(name="Lecture en cours", value=np_str, inline=False)

    q_str = ''
    i = 1
    for item in queue.queue:
        q_str += str(i) + ". " + item.data.get('snippet').get('title') + "\n"
        i += 1
    if q_str == '':
        q_str = 'Aucune musique en attente.'
    res.add_field(name='À venir', value=q_str, inline=False)

    return res


def select_music_embed(items):
    res = embeds.Embed(title="Choisir une musique", type="rich")
    q_str = ''
    i = 0
    for item in items:
        q_str += str(i) + ". " + item.get('snippet').get('title') + "\n"
        i += 1
    if q_str == '':
        q_str = 'Euh wtf.'
    res.add_field(name='Recherche', value=q_str, inline=False)
    return res


def channel_embed(channel):
    subtext = "Cette chaîne cache ses abonnés :(" if channel['statistics']['hiddenSubscriberCount'] \
        else "Cette chaîne possède **{}** abonné(s).".format(channel['statistics']['subscriberCount'])
    description = "{}\nElle a **{}** vues, et **{}** vidéos."\
        .format(subtext, channel['statistics']['viewCount'], channel['statistics']['videoCount'])

    res = embeds.Embed(title=channel['snippet']['title'], type="rich", description=description,
                       url="https://www.youtube.com/channel/{}".format(channel['id']))
    res.set_author(name="YouTube", url="https://youtube.com/",
                   icon_url="https://cdn.discordapp.com/attachments/480416542014701581/484672637751001100/YouTube-icon.png")
    res.set_footer(text=channel['snippet']['description'])
    res.set_thumbnail(url=channel['snippet']['thumbnails']['medium']['url'])
    return res