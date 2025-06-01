# Python
def create_point_system():
    print("""-- Roblox Lua Script (Dari Python)
local Players = game:GetService("Players")

local points = {}

Players.PlayerAdded:Connect(function(player)
    points[player.UserId] = 0
    
    player.CharacterAdded:Connect(function(character)
        local humanoid = character:WaitForChild("Humanoid")
        humanoid.Died:Connect(function()
            points[player.UserId] = points[player.UserId] + 1
            print(player.Name.." sekarang memiliki "..points[player.UserId].." poin")
        end)
    end)
end)
""")

create_point_system()
