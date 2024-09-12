## Баг Репорт

**Название:** Ошибка фильтрации игр по категории в тесте test_filter_category

**Описание:** При фильтрации по категориям (MMORPG, Shooter, Strategy, MOBA, Racing, Sports, Social) обнаружены игры, которые не соответствуют ожидаемому жанру.

**Приоритет:** Высокий

**Среда выполнения:**

- Браузер: Chrome
- Версия Selenium WebDriver: 4.24.0
- Версия Python: 8.3.2
- Операционная система: Windows 11

**Шаги для воспроизведения:**

1. Запустить тест test_filter_category с параметрами категорий: MMORPG, Shooter, Strategy, MOBA, Racing, Sports, Social и ожидаемых жанров.

Тест проходит следующие действия:
1. Переходит на главную страницу.
2. Выбирает указанную категорию.
3. Проверяет все страницы на наличие игр с неправильным жанром.

**Ожидаемый результат:** Все игры, отображаемые в выбранной категории, должны соответствовать ожидаемому жанру.

**Фактический результат:** В категориях (MMORPG, Shooter, Strategy, MOBA, Racing, Sports, Social) обнаружены игры, которые не соответствуют ожидаемому жанру.

| №  | Категория | Игры, которые не соответствуют выбранной категории |
|----|-----------|----------------------------------------------------|
| 1  | MMORPG    | Destiny 2 (Shooter), Once Human (Shooter), Waven (Strategy), Blankos Block Party (MMO), Fer.al (MMO), Stay Out (Shooter), Firestone Idle RPG (Strategy), Dungeon Fighter Online (Fighting), Cubic Castles (MMO), Creativerse (MMO), Roblox (MMO) |
| 2  | Shooter   | Predecessor (MOBA), Project Apidom (MOBA), Deceit 2 (Action), Super Squad (MOBA), Blankos Block Party (MMO), Spellbreak (Battle Royale), Will To Live (MMORPG), The Ultimatest Battle (Fighting), Awesomenauts (MOBA), Heavy Metal Machines (MOBA), UFO Online: Invasion (MMORPG), Starbreak (MMORPG), Robocraft (MMO), Archeblade (Fighting), Pocket Starships (Strategy), Panzar (MOBA), Dino Storm (MMORPG), Realm of the Mad God (MMORPG) |
| 3  | Strategy  | Destiny's Divide (Card Game), Warhammer 40,000: Warpforge (Card Game), Warlander (MOBA), Fangs (MOBA), Marvel Snap (Card Game), Magic Spellslingers (Card Game), Temperia: Soul of Majestic (Card Game), Super Squad (MOBA), Chroma: Bloom And Blight (Card Game), Eternal Return: Black Survival (MOBA), Bombergrounds: Battle Royale (Battle Royale), Legends of Runeterra (Card Game), Mythgard (Card Game), Minion Masters (Card Game), Kards (Card Game), Artifact (Card Game), Magic: The Gathering Arena (Card Game), League of Angels 3 (MMORPG), Cosmos Invictus (Card Game), Spellsworn (MOBA), Gwent: The Witcher Card Game (Card Game), Catan Universe (Card Game), Krosmaga (Card Game), Chronicles of Eidola (MMORPG), Cabals: Card Blitz (Card Game), One Tower (MOBA), Shadowverse (Card Game), Battlerite (MOBA), Star Crusade (Card Game), The Elder Scrolls: Legends (Card Game), Naruto Online (MMORPG), UFO Online: Invasion (MMORPG), Dragon Blood (MMORPG), League of Angels 2 (MMORPG), Astral Heroes (Card Game), Spellweaver (Card Game), Immortal Empire (MMORPG), One Piece Online 2 (MMORPG), Card Hunter (Card Game), Heroes of the Storm (MOBA), Pox Nora (Card Game), WAKFU (MMORPG), Infinity Wars (Card Game), Hex (Card Game), Hearthstone: Heroes of Warcraft (Card Game), Dota 2 (MOBA), Epic Cards Battle (Card Game), Wartune (MMORPG), RPG MO (MMORPG), Steel Legions (Shooter), Bloodline Champions (MOBA), League of Legends (MOBA), Atlantica Online (MMORPG), Urban Rivals (Card Game), Dofus (MMORPG) |
| 4  | MOBA      | Blood of Steel (Strategy), Crystal Clash (Strategy), Minion Masters (Card Game), Battle Arena Heroes Adventure (Strategy), Paladins (Shooter), Dungeon Defenders 2 (Shooter), Divine Souls (MMORPG), Robocraft (MMO), Archeblade (Fighting), Pocket Starships (Strategy), Dogs of War Online (Strategy), AirMech (Strategy) |
| 5  | Racing    | Grand Prix Racing Online (Strategy) |
| 6  | Sports    | Forza Motorsport 6: Apex (Racing), Grand Prix Racing Online (Strategy) |
| 7  | Social    | Roblox (MMO) |

