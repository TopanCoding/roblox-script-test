from roblox import RobloxClient
import asyncio

async def join_game():
    client = RobloxClient(".ROBLOSECURITY_COOKIE")
    game_id = 987654321  # change to game id
    
    # Join game
    join_url = await client.get_game_join_url(game_id)
    print(f"Join URL: {join_url}")
    
    # open in browser (opsional)
    import webbrowser
    webbrowser.open(join_url)

asyncio.run(join_game())
