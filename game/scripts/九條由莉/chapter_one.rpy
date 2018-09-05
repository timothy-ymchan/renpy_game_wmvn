label yuri_chapter_one:
    scene bg park_night with dissolve
    "離開補習社之時，經已是夜深"
    "大概又是以便利店便當作為晚餐吧。"

    scene bg convenience_store with dissolve
    "即使進入了晚上，地上還仍然殘留着上午日照的餘温。"
    player "「今天真熱呢，買根冰條作飯後甜品吧。」"

    "店員" "「歡迎光臨!」"

    "我走進了便利店內，在冰品櫃前挑選着心誼的冰條。"

    player "「草莓、芒果、巧克力…款色真多呢，選哪款好呢?」"


    show yuri normal
    yuri "「拿不到呀…哪裏有人來幫忙啊…」"

    "飲品櫃處傳來求助的聲音，一眼望去，是一個女孩。"

    menu:
        "你要幫她嗎？"

        "幫助她吧":
            "我走到那個女孩的身旁"
            yuri "「那個，幫我拿在貨架頂上的可樂吧。」"
            "我跳起身來，把可樂拿到手上。"

        "先買雪條吧":
            "當我正繼續凝視冰品櫃時，那個女孩轉過頭來，"
            "與我搭上了視線。"
            yuri "「那個…可以幫我拿在貨架頂上的可樂嗎?」"
            "我走到那個女孩的身旁，"
            "跳起身來，把可樂拿到手上。"


    player "「啊」"

    scene bg some_fan_service_scene with hpunch
    "在落地的一刻，失了重心，把她推倒了"
    yuri "「啊!很痛」"
    "她撞到身後的貨架，貨物壓在我們身上"

    player "「非常抱歉，你有受傷嗎?」"

    "我趕緊從她的身上移開"
    "映入眼簾的卻是意外掀起了的裙子"

    player "「……」"
    "雖然討厭語文，但非禮勿視的基本紳士風範，我還是懂的"
    "我趕緊轉開頭，分散自己的注意力。"

    "她看看我慌張的模樣，再看看自己的裙子"
    "臉上通紅了一片"
    "然後急忙用手把裙子拉好"

    scene bg some_scene_with_yuri_angry_look with dissolve
    yuri "「你在看哪裡啦，變態」"
    player "「我才沒有看呀」"

    scene bg convenience_store with dissolve
    "我瞥見了她流血的左手手臂，應該是被摔破的玻璃瓶弄傷了吧"
    player "「你的手臂，沒事吧？」"
    show yuri normal with dissolve
    yuri "「很痛呀，都是你害的啦」"
    yuri "「我家就在旁邊，去幫我包紮的話便原諒你吧」"
    player "「孤男寡女，不太恰當的吧…」"
    yuri "「嘈死了，你還是不是男人啊，婆婆媽媽的」"

    "我把掉落的貨物快速收拾好，向店員道了歉"
    "急忙離開了便利店。"

    scene bg yuri_house_night with dissolve
    "到達了女孩的家，門牌上寫著「九條」兩個字"

    show yuri normal with dissolve
    yuri "「這裏就是我的家了，快點幫我包紮呀」"
    "她邊説着，邊從櫃裏拿出急救傷。"

    "我細心地幫她消毒及包紮傷口"
    player "「會有點痛的，忍着哦」"
    yuri "「嗯...呀，很痛呀」"

    player "「行了，包紮完了」"
    yuri "「還包紮得不錯，那就先原諒你吧」"

    show yuri normal with hpunch
    "(…震機聲…)"
    "我把手機拿了出來，卻被她一手搶走了"
    "她打了幾個字，然後還了給我"

    $yuri.next_name()
    "聯絡人上多了一個名為「九條由莉」的人"
    yuri "「我叫九條由莉，不要忘記哦」\n"
    extend  "「忘記的話...，"
    extend "就把你殺了」(小聲)"

    player "「甚麼？」"
    "總感覺到背部傳來一陣冷風"

    yuri "「沒啦，總之不要忘記我啦」"

    "我看一看手機右上角的時鐘"
    player "「糟糕了!已經這麼晚了嗎?」"
    player "「抱歉，我要回家了，再見。」"
    yuri "「再見。」"

    hide yuri with dissolve

    "我跑出了九條家，踏上回家的路途"
    "總算回到了家中，"

    scene bg room with dissolve
    "然而家中空無一人，父母都在外地工幹着"
    player "「糟糕，我便當也忘了買啊…」"
    player "「功課也還多着…」"
    player "「怎麼辦才好? 」"

return
