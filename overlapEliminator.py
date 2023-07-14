#import re

#pattern = r'^\d+\s+[\w-]+\s+(?:[\w-]+\s+)?[\w-]+\s+(?:(\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3})\s+)?(?:\d+\s+)?(?:[\w-]*\s+)?(?:[\w-]+\s+)?((?:\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3})?)?\s*$'

data = '''001 Arjun Karnwal akarnwal23@mylcusd.net 088 Sudha Karnwal sudha94@yahoo.com
002 Christopher Kurdoghlian Ckurdoghlian23@mylcusd.net 089 Araa Araarpi@yahoo.com
003 Robyn Lam robynjmlam@gmail.com 090 Edward Lam ewhl@yahoo.com
004 Warren Lam wlam23@mylcusd.net 091
005 Imogen Lee ilee23@mylcusd.net 092 Brenda Lee brendaquon@hotmail.com
006 Giselle Ng gng@lacanadaengineeringclub.org 093 Michelle Ng mailgks8@gmail.com
007 Nicholas Reinoso ncr4014@gmail.com 094 Jennifer Langan jennifer.l.langan@gmail.com
008 Kourosh Salahi Kouroshandrew@yahoo.com 095 R Salahi r_salahi@yahoo.com
009 siraaj Sandu ssandhu23@mylcusd.net 096 Jagmit Sandhu jagmit.sandhu@gmail.com
010 Aiden Wang awang2320@mylcusd.net 097 Kathy Wang centralstreet@yahoo.com
011 Madison Ward mpward5000@gmail.com 098 Leslie Ward lward@hl.com
012 Haochen Yang hyang23@mylcusd.net 099 I Yang lydiaxieyang@gmail.com
013 Jeshurun Liou jliou23@mylcusd.net 100 Joyce Liou joycec2@yahoo.com
014 Charlie Khanlarian ckhanlarian23@mylcusd.net 101 Mrs. Khanlarian ekhanlarian@lcusd.net
015 David Backer Peral davidbperal@gmail.com 102 Eva Peral evamperal@gmail.com
016 Sanjith Cherumandanda scherumandanda24@mylcusd.net 103 Subbaiah Cherumandanda subbaiah@yahoo.com
017 Grady Conwell gradyconwell@iclould.com 104 Christina Conwell christinaconwell@mac.com
018 Victor He vh95vvhh@gmail.com 105 Mei He ccmm1111cm@gmail.com
019 Josh Sugino jsugino@lacanadaengineeringclub.org 106 Scott Sugino kunitachi39@gmail.com
020 Linus Sun linusrsun@gmail.com 107 Peter Sun Lscpks@gmail.com
021 Patrick Thuss pdthuss@icloud.com 108 Octavia Thuss Octavia_howell@yahoo.com
022 Noah Balderston Balderstonnoah@gmail.com 109 Julia Wood Juliawoodmusic@gmail.com
023 Louis Chang-Johnson LChangJohnson27@myLCUSD.net110 Melody Chang Glenn.and.melody@mac.com
024 Leo Chaudhary-Kim leoslegos1@gmail.com 111 Mrs. Kim kimsykim1@gmail.com
025 brandon chun Brandonchun4444@gmail.com 112 Chun Family hjyw63112@gmail.com
026 Connor Chung cchung2611@mylcusd.net 113 Tara Thacker Tarathacker@gmail.com
027 Paulina Danilova pdanilova@gmail.com 114 Olga Danilova olgadan@gmail.com
028 Trentan Dave trentandave1@gmail.com 115 Karen Dave aukaren1@gmail.com
029 Leon Holloway goshawk.holloway@gmail.com 116 Alexandra Holloway alexandra.holloway@gmail.com
030 Richard Hong richardhong2007@gmail.com 117 Tina Hong tinaye0517@gmail.com
031 Annabelle Hsieh hsiehannabelle2024@gmail.com 118 Sonya Hsieh sonyachsieh@gmail.com
032 Min Hwang mhwang1214@gmail.com 119 Neush neush@naver.com
033 Joanne Kim joannek3700@gmail.com 120 Injalee injalee1999@gmail.com
034 Alexander Konakov alexanderkjedi@gmail.com 121 Maxim Konakov mkonakov@yahoo.com
035 Alyssa Konakov alyssakjedi@gmail.com 122 Mijung Konakov mjkonakov@gmail.com
036 Jakob Konefat konefatjakob@gmail.com 123 Konefat Family konefatfamily@gmail.com
037 Akhilesh Kumar akhileshk2031@gmail.com 124 Santhiiyerkumar santhiiyerkumar@gmail.com
038 Calliope Lee calliopelee205@gmail.com 125 Angela Lee angelleehappy@gmail.com
039 Chloe Lee clee@lacanadaengineerinclub.org 126
040 Christopher Lee clee2605@mylcusd.net 127
041 Kenneth (Kenny) Lee kenjlee09@gmail.com 128 Jenji Lee jenjlee@gmail.com
042 Milo Lin Mlin27@mylcusd.net 129 Eric Lin Ericl@infiniocapital.com
043 Gabriel Park gpark28@mylcusd.net 130 Jayn Park parkjayn@gmail.com
044 Noah Park npark28@mylcusd.net 131
045 Sean Piapakdee spiapakdee26@mylcusd.net 132 S Pisapakdee spiapakdee@gmail.com
046 Thomas Qin 133
047 Logan Quon lquon25@mylcusd.net 134 Jayne Hua jayne_hua@hotmail.com
048 Mateo Rose David.rose.h2o@gmail.com 135 gisgalan rose gisgalan@protonmail.com
049 Jessica Simonian Jessicasimonian@gmail.com 136 Fred Simonian Fredsimonian@hotmail.com
050 Evan Skelton evanskelton177@gmail.com 137 Nancy Skelton loveisfamily@charter.net
051 Eli Street estreet27@mylcusd.net 138 rsw rws173@yahoo.com
052 Celeste Tarula ctarulavillarreal25@mylcusd.net 139 fortino fortino@allomatic.net
053 Sean Toda seantoda4@gmail.com 140 Risaku Toda risaku.toda@gmail.com
054 Miles Worster milesworster@gmail.com 141 Whitney Whitneyworster@gmail.com
055 Amy Avanessian amy.m.avanessian@gmail.com 142 Stepanie Avanessian stephanie.avanessian@gmail.com
056 Lucy Avanessian lucy.avanessian@gmail.com 143
057 Eleanora Brutocao 144 L Brutocao ltbrutocao@gmail.com
058 Preston Chang-Johnson 145
059 Jaelyn Chung jaelynchung@icloud.com 146 I Chung l.chung@lcusd.net
060 Hudson Chung 147
061 Jacob Fraund 148 Fraund mayee08@yahoo.com
062 Jacqueline Garnic 149 Nehcarul nehcarual@gmail.com
063 Jack Haber 150 Lisa Haber Iisa_haber@att.net
064 Beatrix Hamlington bhamlington@gmail.com 151
065 Trevor Hatch thatch28@mylcusd.net 152 Sara Jean sarajean22@gmail.com
066 Jasmine Hoang jhoang28@mylcusd.net 153 Ellis Meng ellis.meng@gmail.com
067 Caesar Hu 154 Lily Liao Lily_liao@hotmail.com
068 Yash Jaju 155 Jajugirish jajugirish@gmail.com
069 Benjamin Kim edamykim@gmail.com 156
070 Ty Koo 157 Kayla Song klasong@yahoo.com
071 TJ Koo 158
072 Jessica Koo 159
073 Ian Lee ianjoonhyuklee@gmail.com 160 Doyouk doyounk@gmail.com
074 Matthew Lee 161 Annie Kim anniekim78@gmail.com
075 Chloe Liang 162 Michelle Yawen yawenmichelle@gmail.com
076 Alex Lin 163 Aklyi akyli@yahoo.com
077 Jeffery Lue 164 Sharon Park bopark206@gmail.com
078 Connor Ng 165 Ng Family treasureshell@yahoo.com
079 Torsten Ouwersloot 166 Nancy Ouwersloot nzwinkels@gmail.com
080 Jason Roth jasonmroth11@gmail.com 167 Darren Roth darrenjroth@yahoo.com
081 Chloe Sui 168 Yong Sui yongsui78@gmail.com
082 Ce Tang CTang28@mylcusd.net 169 Julia Wu juliawu2006@gmail.com
083 Jane Tang janej111208@gmail.com 170
084 Andrew Tran 171 Jennifer Tran jennifert2017@gmail.com
085 Katelyn Tran 172
086 Nick Wood 173 Julie Wood woodfamily1126@gmail.com
087 Emily Yoo 174 Kjlee Kjlee28@gmail.com'''

# matches = re.findall(pattern, data, re.MULTILINE)
# 
# pemails = ", ".join(match[1] for match in matches if match[1])
# 
# print(pemails)
# 
# count = 0
# for char in pemails:
#     if char == ',':
#         count += 1
# print("emails: ", count+1)

# -----------------------------------------------------
# CHATGPT IS NOT STEALING MY JOB YET MUAHAHAHAHAHA!!!

pemails = []
for line in data.splitlines():
    numbers = 0
    at_index = -1
    just_saw_digit = False

    for index, char in enumerate(line):
        if just_saw_digit and char == " ": # We've a valid ID number
            numbers += 1

        if char.isdigit():
            just_saw_digit = True
        else: just_saw_digit = False

        if char == "@" and numbers == 2:
            # This is the right @
            at_index = index
    
    words = line.split()
    if at_index > -1:
        for word in words:
            if at_index >= line.index(word) and at_index < line.index(word) + len(word):
                pemails.append(word)

output = ", ".join(pemails)
print(output)
