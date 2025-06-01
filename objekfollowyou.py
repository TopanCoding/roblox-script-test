def create_follow_script():
    print("""-- Roblox Lua Script (Dari Python)
local RunService = game:GetService("RunService")
local object = script.Parent
local target = nil

game.Players.PlayerAdded:Connect(function(player)
    player.CharacterAdded:Connect(function(character)
        target = character:WaitForChild("HumanoidRootPart")
    end)
end)

RunService.Heartbeat:Connect(function()
    if target then
        object.Position = target.Position + Vector3.new(0, 5, 0)
    end
end)
""")

create_follow_script()
