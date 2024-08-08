def create_game(game_id: int, title: str = 'Test', views: int = 0, downloads: int = 0, purchases: int = 0):
    return {
        'id': game_id,
        'title': title,
        'views_count': views,
        'downloads_count': downloads,
        'purchases_count': purchases
    }
