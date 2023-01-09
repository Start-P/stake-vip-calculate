import disnake
from disnake.ext import commands
from calc import StakeCalculator

bot = commands.InteractionBot()

with open("token.txt") as f:
    token = f.read().splitlines()[0]

@bot.slash_command(
    name="stake_calculator",
    description="レベルアップまでに必要な金額などを見ることができます。",
    options=[
        disnake.Option(
            name="progress",
            description="現在の進捗率を数字で入力してください。",
            type=disnake.OptionType.number,
            required=True,
        ),
        disnake.Option(
            name="rank",
            description="現在のランクを選択してください。",
            type=disnake.OptionType.string,
            required=True,
            choices=[
                disnake.OptionChoice(
                    name="ブロンズ",
                    value="bronze"
                ),
                disnake.OptionChoice(
                    name="シルバー",
                    value="silver"
                ),
                disnake.OptionChoice(
                    name="ゴールド",
                    value="gold"
                ),
                disnake.OptionChoice(
                    name="プラチナ",
                    value="platinum"
                ),
                disnake.OptionChoice(
                    name="プラチナII",
                    value="platinum2"
                ),
                disnake.OptionChoice(
                    name="プラチナIII",
                    value="platinum3"
                ),
                disnake.OptionChoice(
                    name="プラチナIV",
                    value="platinum4"
                ),
                disnake.OptionChoice(
                    name="プラチナV",
                    value="platinum5"
                ),
                disnake.OptionChoice(
                    name="プラチナVI",
                    value="platinum6"
                ),
                disnake.OptionChoice(
                    name="ダイヤモンド",
                    value="diamond"
                ),
            ]
        )
    ]
)
async def slash_calc(inter, progress: float, rank):
    stake_calc = StakeCalculator(rank, progress)
    required_percent, required_dollars = stake_calc.calc()
    embed = disnake.Embed(
        title="計算結果",
        description="レベルアップに必要な賭け金を計算することができます。",
        color=disnake.Colour.red(),
    )

    embed.set_author(
        name=inter.user.name,
        icon_url=inter.user.avatar.url
    )

    embed.add_field(name="現在のランク", value=rank.capitalize())
    embed.add_field(name="レベルアップまで残り", value=f'{str(required_percent)}％')
    embed.add_field(name="必要な賭け金", value=f"${str(required_dollars)}")

    await inter.response.send_message(embed=embed)


@bot.event
async def on_ready():
    print("Running as : " + bot.user.name)

if __name__ == "__main__":
    bot.run(token)

