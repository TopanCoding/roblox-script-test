def create_gui_script():
    print("""-- Roblox Lua Script (Dari Python)
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local gui = script.Parent
local button = gui:WaitForChild("TextButton")
local points = 0

button.MouseButton1Click:Connect(function()
    points = points + 1
    button.Text = "Poin: "..points
    
    if points >= 10 then
        button.TextColor3 = Color3.new(0, 1, 0)
    end
end)
""")

create_gui_script()
