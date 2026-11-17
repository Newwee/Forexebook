import json
import os

os.makedirs(r"C:\Users\New JA\Downloads\EbookFOREX\src\data", exist_ok=True)

script_content = """import { Chapter, GlossaryTerm, Scenario } from '../types'

export const CHAPTERS: Chapter[] = [
  {
    id: 'ch-01-forex-basics',
    chapterNumber: 1,
    title: 'ปูพื้นฐานตลาด Forex & ผู้เล่นในตลาด (Market Participants)',
    englishTitle: 'Forex Foundations & Smart Money vs Retail',
    category: 'Foundations',
    difficulty: 'Beginner',
    estimatedMinutes: 15,
    pdfPages: '3 - 7',
    shortDescription: 'ทำความเข้าใจประชากรในตลาด ใครเป็นคนขับเคลื่อนกราฟจริง และหลักการจับคู่เงิน Forex ที่ถูกต้อง',
    whyItMatters: 'หากคุณไม่รู้ว่าใครคุมตลาด คุณจะตกเป็นเหยื่อของ Smart Money ตลาด Forex ขับเคลื่อนด้วยเม็ดเงินของสถาบันการเงิน ไม่ใช่รายย่อย',
    summary: [
      'ตลาด Forex ประกอบด้วย ธนาคารกลาง, ธนาคารโลก, กองทุน/โบรกเกอร์ใหญ่ (Smart Money) และรายย่อย (Retail)',
      'แรงของกราฟหลักๆ เกิดจากกองทุนใหญ่และธนาคาร รายย่อยไม่สามารถเอาชนะตลาดได้ถ้าเทรดสวนทาง Smart Money',
      'คู่เงินสกุลตัวหน้า (Base Currency) มีค่าเท่ากับ 1 เสมอ ตัวหลังคือ Quote Currency',
      'หากสกุลเงินตัวหลังแข็งค่าขึ้น กราฟจะวิ่งลง หากสกุลเงินตัวหน้าแข็งค่า กราฟจะวิ่งขึ้น'
    ],
    keyTerms: [
      { term: 'Smart Money', meaning: 'กลุ่มสถาบันการเงิน กองทุน และธนาคารกลางที่มีวอลุ่มมหาศาลในการกำหนดทิศทางตลาด' },
      { term: 'Retail Traders', meaning: 'เทรดเดอร์รายย่อยทั่วไป มีจำนวนมากที่สุดในตลาดแต่มีผลต่อทิศทางกราฟน้อยที่สุด' },
      { term: 'Base Currency', meaning: 'สกุลเงินหลักที่อยู่ตัวหน้า มีค่าเท่ากับ 1 เสมอ เช่น EUR ใน EUR/USD' },
      { term: 'Quote Currency', meaning: 'สกุลเงินอ้างอิงที่อยู่ตัวหลัง บ่งบอกว่าต้องใช้เงินสกุลนี้เท่าไรแลก 1 หน่วยของตัวหน้า' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_003.png',
        caption: 'หน้า 3: ประชากรในตลาด Forex (ธนาคารกลาง, ธนาคารโลก, กองทุน, รายย่อย)',
        page: 3
      },
      {
        url: '/extracted/page_renders/page_004.png',
        caption: 'หน้า 4: แรงขับเคลื่อนของกราฟมาจากกลุ่มกองทุนใหญ่',
        page: 4
      },
      {
        url: '/extracted/page_renders/page_005.png',
        caption: 'หน้า 5: โครงสร้างคู่เงิน Forex (Base Currency = 1 เสมอ)',
        page: 5
      },
      {
        url: '/extracted/page_renders/page_007.png',
        caption: 'หน้า 7: การเปรียบเทียบมูลค่าสกุลเงินและการส่งผลต่อกราฟ',
        page: 7
      }
    ],
    lessons: [
      {
        id: 'lesson-1-1',
        title: 'ใครคือผู้กำหนดทิศทางตลาด Forex ที่แท้จริง?',
        content: `ในตลาด Forex มีประชากร 4 กลุ่มหลัก:
1. **ธนาคารกลาง (Central Banks):** ผู้กำหนดนโยบายการเงิน อัตราดอกเบี้ย และพิมพ์ธนบัตร
2. **ธนาคารโลก (World Bank) & สถาบันการเงินระหว่างประเทศ:** บริหารทุนสำรองระหว่างประเทศ
3. **กองทุนเฮดจ์ฟันด์และสถาบันการเงินรายใหญ่ (Hedge Funds & Institutional Brokers):** Smart Money ผู้มีสภาพคล่องและเครื่องมืออัลกอริทึม
4. **ประชากรทั่วไป (Retail Traders):** พวกเราเทรดเดอร์รายย่อย

**ความจริงสำคัญจาก E-Book (หน้า 3-4):**
ประชากรทั่วไปมี "จำนวนคนมากที่สุดในตลาด" แต่มี "แรงผลักดันราคาน้อยที่สุด" ในทางกลับกัน สถาบันการเงินและธนาคารมีจำนวนน้อย แต่ถือครองเม็ดเงินมหาศาลจนเป็นผู้สร้าง "แรงของกราฟ" (Impulse Move)

ดังนั้น เป้าหมายของการเรียนรู้ระบบ SMC คือการเลิกเทรดแบบรายย่อย และเปลี่ยนมาแกะรอยการเคลื่อนไหวของ Smart Money เพื่อเกาะกระแสไปกับเงินก้อนโต`,
        corePrinciples: [
          'รายย่อยมีจำนวนมากที่สุด แต่ไม่มีแรงขยับกราฟ',
          'แรงผลักดันกราฟทั้งหมดมาจากธนาคารและกองทุนใหญ่',
          'ห้ามเทรดสวนทาง Smart Money เพราะเราไม่สามารถเอาชนะสภาพคล่องของกองทุนได้'
        ],
        practicalExamples: 'เมื่อมีข่าว Non-Farm หรือการประชุม FOMC กราฟพุ่งทะลุ 100-200 จุดในไม่กี่นาที นั่นคือจังหวะที่ธนาคารและอัลกอริทึมส่งคำสั่งซื้อขายก้อนมหึมาเข้าสู่ตลาด',
        proTips: 'อย่าพยายามเป็นคนกลับตัวกราฟ ให้รอ Smart Money แสดงเจตนาผ่านโครงสร้างตลาดก่อน แล้วจึงเข้าออเดอร์ตาม',
        pitfalls: 'การคิดว่าแรงซื้อของรายย่อยรวมกันจะช่วยดันกราฟขึ้นได้ ซึ่งไม่เป็นความจริงในตลาดที่มีวอลุ่ม 7.5 ล้านล้านดอลลาร์ต่อวัน'
      },
      {
        id: 'lesson-1-2',
        title: 'กลไกคู่เงิน Forex: สกุลเงินตัวหน้าเท่ากับ 1 เสมอ',
        content: `การอ่านคู่เงิน Forex จากหน้า 5-7 ของ E-Book:
- ตัวอย่างเช่นคู่ **USD/THB**: สกุลเงินตัวหน้า (USD) จะเท่ากับ 1 เสมอ แปลว่า **1 ดอลลาร์สหรัฐ แลกได้ 36.832 บาท**
- ในคู่ **EUR/USD**: EUR คือ Base Currency (ตัวหน้า = 1) และ USD คือ Quote Currency (ตัวหลัง)
- ในคู่ **USD/JPY**: USD คือ Base Currency (ตัวหน้า = 1) และ JPY คือ Quote Currency (ตัวหลัง)

**กฎการวิ่งของกราฟ (หน้า 6-7):**
1. ถ้าสกุลเงินตัวหลัง (เช่น JPY) มีมูลค่าแข็งค่าขึ้น (Stronger) จะส่งผลให้สกุลเงินตัวหน้า (USD) อ่อนค่าลงโดยอัตโนมัติเมื่อเทียบกัน -> **กราฟ USD/JPY จะปรับตัวลดลง (Down Trend)**
2. ถ้าสกุลเงินตัวหน้า (เช่น EUR) แข็งค่าขึ้น หรือสกุลเงินตัวหลัง (USD) อ่อนค่าลง -> **กราฟ EUR/USD จะพุ่งสูงขึ้น (Up Trend)**`,
        corePrinciples: [
          'สกุลเงินตัวหน้า (Base Currency) มีค่าอ้างอิงเป็น 1 หน่วยเสมอ',
          'ราคาที่เห็นบนหน้าจอ คือมูลค่าของสกุลเงินตัวหลังที่ต้องจ่ายเพื่อซื้อ 1 หน่วยของตัวหน้า',
          'ตัวหน้าแข็ง / ตัวหลังอ่อน = กราฟขึ้น',
          'ตัวหน้าอ่อน / ตัวหลังแข็ง = กราฟลง'
        ],
        practicalExamples: 'หากธนาคารกลางญี่ปุ่น (BOJ) ประกาศขึ้นอัตราดอกเบี้ย เงินเยน (JPY) จะแข็งค่าขึ้นอย่างรวดเร็ว ส่งผลให้กราฟคู่ USD/JPY ร่วงลงอย่างหนัก',
        proTips: 'สังเกตค่าเงินดอลลาร์ (DXY) เป็นหลักเสมอ เพราะดอลลาร์มีผลกับคู่เงินหลักส่วนใหญ่ในโลก',
        pitfalls: 'สับสนว่าตัวไหนเป็นตัวซื้อตัวไหนเป็นตัวขาย จำไว้ว่าเมื่อกด BUY คือเราซื้อตัวหน้าและขายตัวหลัง'
      }
    ],
    quiz: [
      {
        id: 'q1-1',
        type: 'mcq',
        question: 'จาก E-Book ประชากรกลุ่มใดที่มีจำนวนคนมากที่สุดในตลาด Forex แต่มีอิทธิพลต่อแรงขยับกราฟน้อยที่สุด?',
        options: [
          'ธนาคารกลาง (Central Banks)',
          'ธนาคารโลก (World Bank)',
          'นายหน้าและกองทุนขนาดใหญ่ (Hedge Funds)',
          'ประชากรทั่วไปหรือเทรดเดอร์รายย่อย (Retail Traders)'
        ],
        correctIndex: 3,
        explanation: 'หน้า 3-4 ของ E-Book ระบุชัดเจนว่า ประชากรทั่วไปมีจำนวนมากที่สุดในตลาด แต่แรงผลักดันกราฟหลักๆ มาจากธนาคารและกองทุนใหญ่ รายย่อยจึงไม่สามารถเทรดชนะตลาดได้หากเทรดสวนทางกองทุน',
        referenceConcept: 'E-Book หน้า 3-4: ประชากรในตลาด Forex'
      },
      {
        id: 'q1-2',
        type: 'mcq',
        question: 'ในคู่เงิน USD/JPY หากเงินเยน (JPY) มีมูลค่าแข็งค่าขึ้นมาก กราฟ USD/JPY จะมีลักษณะอย่างไร?',
        options: [
          'กราฟจะพุ่งขึ้นทำ Higher High (Up Trend)',
          'กราฟจะปรับตัวลงหรือทิ้งตัวลง (Down Trend)',
          'กราฟจะอยู่นิ่งไม่ขยับเลย',
          'ไม่มีความสัมพันธ์กัน'
        ],
        correctIndex: 1,
        explanation: 'หน้า 7 ของ E-Book ระบุว่า หาก JPY ซึ่งเป็นสกุลเงินตัวหลังแข็งค่าขึ้น จะส่งผลให้ USD อ่อนค่าลงโดยเปรียบเทียบ กราฟจึงมีลักษณะปรับตัวร่วงลง',
        referenceConcept: 'E-Book หน้า 6-7: กลไกคู่เงิน Forex'
      },
      {
        id: 'q1-3',
        type: 'tf',
        question: 'ในคู่เงิน Forex สกุลเงินที่อยู่ข้างหน้า (Base Currency) จะมีค่าเท่ากับ 1 เสมอ จริงหรือไม่?',
        options: [
          'จริง (เช่น USD/THB หมายถึง 1 USD แลกได้กี่บาท)',
          'ไม่จริง สกุลเงินตัวหลังต่างหากที่มีค่าเท่ากับ 1'
        ],
        correctIndex: 0,
        explanation: 'หน้า 5 ของ E-Book ระบุว่า "สกุลเงินที่อยู่ข้างหน้า เท่ากับ 1 เสมอ อย่างเช่น USD/THB ก็คือ 1 ดอลลาร์ เท่ากับกี่บาท"',
        referenceConcept: 'E-Book หน้า 5: โครงสร้างคู่เงิน'
      }
    ]
  },
  {
    id: 'ch-02-market-structure',
    chapterNumber: 2,
    title: 'Market Structure & แนวโน้มของเทรน (โครงสร้างตลาด)',
    englishTitle: 'Market Structure: Up Trend, Down Trend & Sideway',
    category: 'Structure',
    difficulty: 'Beginner',
    estimatedMinutes: 15,
    pdfPages: '8 - 10',
    shortDescription: 'พื้นฐานโครงสร้างตลาด 3 รูปแบบ การระบุ Higher High, Higher Low, Lower High, Lower Low อย่างเป็นระบบ',
    whyItMatters: 'โครงสร้างตลาดคือแผนที่นำทาง หากอ่านโครงสร้างผิด คุณจะเปิดออเดอร์สวนเทรนหลักและโดนล้างพอร์ตทันที',
    summary: [
      'ตลาดมี 3 แนวโน้ม: Up Trend, Down Trend และ Side ways',
      'Up Trend ประกอบด้วยการยก Higher High (HH) และ Higher Low (HL)',
      'Down Trend ประกอบด้วยการกด Lower High (LH) และ Lower Low (LL)',
      'Side ways คือสภาวะที่ราคาไม่มีทิศทางแน่นอน เคลื่อนที่อยู่ในกรอบ'
    ],
    keyTerms: [
      { term: 'Higher High (HH)', meaning: 'จุดสูงสุดใหม่ที่ยกตัวสูงกว่าจุดสูงสุดก่อนหน้า' },
      { term: 'Higher Low (HL)', meaning: 'จุดต่ำสุดใหม่ที่ยกตัวสูงกว่าจุดต่ำสุดก่อนหน้า' },
      { term: 'Lower High (LH)', meaning: 'จุดสูงสุดใหม่ที่ลดระดับต่ำลงกว่าจุดสูงสุดเดิม' },
      { term: 'Lower Low (LL)', meaning: 'จุดต่ำสุดใหม่ที่ลดระดับต่ำลงกว่าจุดต่ำสุดเดิม' },
      { term: 'Sideway', meaning: 'สภาวะราคาไร้ทิศทาง แกว่งตัวในกรอบแนวรับแนวต้าน' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_008.png',
        caption: 'หน้า 8: โครงสร้างตลาด Market Structure',
        page: 8
      },
      {
        url: '/extracted/page_renders/page_009.png',
        caption: 'หน้า 9: รูปแบบของเทรน 3 รูปแบบ (Up Trend, Down Trend, Sideway)',
        page: 9
      },
      {
        url: '/extracted/page_renders/page_010.png',
        caption: 'หน้า 10: สภาวะ Side ways ที่ไม่มีทิศทางแน่นอน',
        page: 10
      }
    ],
    lessons: [
      {
        id: 'lesson-2-1',
        title: '3 รูปแบบของแนวโน้มตลาดและองค์ประกอบสวิง',
        content: `จากหน้า 8-10 ของ E-Book ตลาดการเงินจะเคลื่อนไหวใน 3 สภาวะเสมอ:

1. **Up Trend (แนวโน้มขาขึ้น):**
   - มีการทำจุดสูงสุดใหม่ที่สูงขึ้นเรื่อยๆ เรียกว่า **Higher High (HH)**
   - มีการยกฐานจุดต่ำสุดใหม่ให้สูงขึ้นเรื่อยๆ เรียกว่า **Higher Low (HL)**
   - หน้าที่ของเทรดเดอร์ใน Up Trend คือการมองหาจุดเข้า BUY ที่บริเวณจุดพักตัว (Discount Zone)

2. **Down Trend (แนวโน้มขาลง):**
   - มีการกดจุดต่ำสุดใหม่ให้ต่ำลงเรื่อยๆ เรียกว่า **Lower Low (LL)**
   - มีการกดจุดสูงสุดใหม่ให้ต่ำลงกว่าเดิม เรียกว่า **Lower High (LH)**
   - หน้าที่ของเทรดเดอร์ใน Down Trend คือการมองหาจุดเข้า SELL ที่บริเวณจุดพักตัว (Premium Zone)

3. **Side ways (สภาวะไร้ทิศทาง):**
   - ราคาไม่สามารถสร้าง HH หรือ LL ได้อย่างชัดเจน แต่เคลื่อนไหวแกว่งตัวขึ้นลงในกรอบแคบๆ
   - เป็นช่วงสะสมสภาพคล่อง (Accumulation) ของ Smart Money ซึ่งมือใหม่ควรหลีกเลี่ยง`,
        corePrinciples: [
          'Up Trend ต้องยกทั้ง High และ Low (HH + HL)',
          'Down Trend ต้องกดทั้ง High และ Low (LH + LL)',
          'Side ways คือช่วงสร้างสภาพคล่อง ห้ามเทรดจนกว่าจะมีทิศทางชัดเจน'
        ],
        practicalExamples: 'เมื่อราคาวิ่งทำ HH ต่อเนื่อง 3 สวิง แต่ละสวิงยกตัวสูงขึ้น การหาจังหวะ Buy เมื่อราคาย่อตัวลงมาจะให้ความได้เปรียบทางสถิติสูงที่สุด',
        proTips: 'ใน SMC เราไม่ได้มองสวิงด้วยสายตาเปล่า แต่เราจะใช้เงื่อนไข Valid Pullback และ IDM ในการยืนยันว่าจุดนั้นเป็น HH หรือ LL ที่แท้จริงหรือไม่',
        pitfalls: 'รีบสรุปว่าเป็น Up Trend เพียงเพราะเห็นแท่งเขียวยาวแท่งเดียว โดยไม่ได้ดูโครงสร้างสวิงภาพรวม'
      }
    ],
    quiz: [
      {
        id: 'q2-1',
        type: 'mcq',
        question: 'ในสภาวะ Up Trend (เทรนขาขึ้น) โครงสร้างสวิงที่ถูกต้องจะต้องประกอบด้วยอะไร?',
        options: [
          'Lower High (LH) และ Lower Low (LL)',
          'Higher High (HH) และ Higher Low (HL)',
          'การเคลื่อนที่แบบไม่มีทิศทางในกรอบแคบ',
          'การทำ Double Top เสมอ'
        ],
        correctIndex: 1,
        explanation: 'หน้า 9 ของ E-Book แสดงโครงสร้าง Up Trend ว่าประกอบด้วยการสร้าง Higher High (HH) และการยกฐาน Higher Low (HL)',
        referenceConcept: 'E-Book หน้า 9: Up Trend Structure'
      },
      {
        id: 'q2-2',
        type: 'mcq',
        question: 'สภาวะ Side ways มีลักษณะสำคัญอย่างไรตาม E-Book หน้า 10?',
        options: [
          'ราคาพุ่งขึ้นอย่างรุนแรงด้วย Impulse Wave',
          'ราคาทำ New Low ต่อเนื่องกัน 5 สวิง',
          'ราคาไม่มีทิศทางที่แน่นอน หรือเคลื่อนที่อยู่ในกรอบ',
          'ราคามีการเบรค BOS ด้วยเนื้อเทียนทุกแท่ง'
        ],
        correctIndex: 2,
        explanation: 'หน้า 10 ระบุว่า "Side ways คือสภาวะที่ราคาไม่มีทิศทางที่แน่นอน หรือเคลื่อนที่อยู่ในกรอบ"',
        referenceConcept: 'E-Book หน้า 10: Side ways'
      }
    ]
  },
  {
    id: 'ch-03-demand-supply',
    chapterNumber: 3,
    title: 'Demand & Supply Zone (โซนอุปสงค์และอุปทาน)',
    englishTitle: 'Supply & Demand Zones: DBR, RBR, RBD, DBD',
    category: 'Foundations',
    difficulty: 'Beginner',
    estimatedMinutes: 20,
    pdfPages: '11 - 18',
    shortDescription: 'เจาะลึก 4 รูปแบบ Demand และ Supply: DBR, RBR, RBD, DBD พร้อมวิธีตีกรอบโซนที่ถูกต้อง',
    whyItMatters: 'Demand & Supply คือจุดต้นกำเนิดของแรงซื้อขาย หากระบุ Base ผิด คุณจะเข้าออเดอร์กลางทางและโดนลาก',
    summary: [
      'Demand คือ ความต้องการซื้อ (เมื่อราคาลงมาถึงจุดนี้จะมีแรงซื้อผลักดันขึ้น)',
      'Supply คือ ความต้องการขาย (เมื่อราคาขึ้นมาถึงจุดนี้จะมีแรงขายกดดันลง)',
      'Base คือ การที่กราฟพักตัว ออกข้าง หรือชะลอความเร็วเพื่อสะสมแรง',
      'Demand มี 2 รูปแบบ: Drop Base Rally (DBR) และ Rally Base Rally (RBR)',
      'Supply มี 2 รูปแบบ: Rally Base Drop (RBD) และ Drop Base Drop (DBD)',
      'การตีกรอบโซน ให้ครอบคลุมส่วนที่มีการ Base ออกข้างรวมถึงไส้เทียนทั้งหมด'
    ],
    keyTerms: [
      { term: 'Demand Zone', meaning: 'โซนที่มีคำสั่งซื้อสะสมหนาแน่น ผลักดันราคาให้พุ่งขึ้น' },
      { term: 'Supply Zone', meaning: 'โซนที่มีคำสั่งขายสะสมหนาแน่น กดราคาให้ร่วงลง' },
      { term: 'Base', meaning: 'แท่งเทียนพักตัวออกข้างก่อนเกิดการระเบิดของราคา' },
      { term: 'DBR (Drop Base Rally)', meaning: 'ราคาร่วงลงมา -> สร้างฐาน Base -> พุ่งขึ้นรุนแรง (รูปแบบกลับตัว Demand)' },
      { term: 'RBR (Rally Base Rally)', meaning: 'ราคาพุ่งขึ้น -> พักตัว Base สั้นๆ -> พุ่งขึ้นต่อ (รูปแบบตามเทรน Demand)' },
      { term: 'RBD (Rally Base Drop)', meaning: 'ราคาพุ่งขึ้นมา -> สร้างฐาน Base -> ทิ้งตัวลงรุนแรง (รูปแบบกลับตัว Supply)' },
      { term: 'DBD (Drop Base Drop)', meaning: 'ราคาร่วงลงมา -> พักตัว Base สั้นๆ -> ทิ้งตัวลงต่อ (รูปแบบตามเทรน Supply)' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_011.png',
        caption: 'หน้า 11: นิยามของ Demand (ความต้องการซื้อ) และ Supply (ความต้องการขาย)',
        page: 11
      },
      {
        url: '/extracted/page_renders/page_013.png',
        caption: 'หน้า 13: ตัวอย่าง Base คือการที่กราฟพักตัว',
        page: 13
      },
      {
        url: '/extracted/page_renders/page_014.png',
        caption: 'หน้า 14: Demand รูปแบบที่ 1: Drop Base Rally (DBR)',
        page: 14
      },
      {
        url: '/extracted/page_renders/page_015.png',
        caption: 'หน้า 15: Demand รูปแบบที่ 2: Rally Base Rally (RBR)',
        page: 15
      },
      {
        url: '/extracted/page_renders/page_016.png',
        caption: 'หน้า 16: Supply รูปแบบที่ 1: Rally Base Drop (RBD)',
        page: 16
      },
      {
        url: '/extracted/page_renders/page_017.png',
        caption: 'หน้า 17: Supply รูปแบบที่ 2: Drop Base Drop (DBD)',
        page: 17
      },
      {
        url: '/extracted/page_renders/page_018.png',
        caption: 'หน้า 18: วิธีการตีกรอบ Demand & Supply Zone รวมไส้เทียน',
        page: 18
      }
    ],
    lessons: [
      {
        id: 'lesson-3-1',
        title: 'ทำความเข้าใจ Demand & Supply และ Base',
        content: `จากหน้า 11-13 ของ E-Book:
- **Demand (ความต้องการซื้อ):** โซนที่กลุ่มผู้ซื้อในตลาดมองว่าราคา "ถูก" และเข้ามาผลักดันราคาให้สูงขึ้น
- **Supply (ความต้องการขาย):** โซนที่กลุ่มผู้ขายในตลาดมองว่าราคา "แพง" และเทขายทำกำไรหรือเปิด Sell
- **Base (การพักตัว):** การที่กราฟหยุดการเคลื่อนที่ในทิศทางเดิม แล้วแกว่งตัวออกด้านข้างเป็นกลุ่มแท่งเทียนเล็กๆ เพื่อสะสมคำสั่งซื้อขายก่อนที่สถาบันจะส่งไม้ใหญ่`,
        corePrinciples: [
          'Demand เกิดขึ้นในจุดที่แรงซื้อชนะแรงขายอย่างเบ็ดเสร็จ',
          'Supply เกิดขึ้นในจุดที่แรงขายชนะแรงซื้ออย่างเบ็ดเสร็จ',
          'Base คือจุดสะสมพลังงานก่อนเกิดการเคลื่อนที่ระเบิดออก'
        ],
        practicalExamples: 'เมื่อราคาวิ่งลงมาอย่างรวดเร็ว แล้วเกิดแท่งเทียนไซด์เวย์ 2-3 แท่ง จากนั้นแท่งถัดไปเป็นแท่งเขียวยาวพุ่งขึ้น นั่นคือจุดกำเนิดของ Demand โซน',
        proTips: 'ยิ่ง Base มีจำนวนแท่งเทียนน้อย (1-3 แท่ง) และตามด้วยแท่งส่งที่ยาวแรง โซนนั้นจะมีคุณภาพสูงกว่า Base ที่ยืดเยื้อนาน',
        pitfalls: 'ตีกรอบ Base กว้างเกินไปจนครอบคลุมทั้งคลื่น ทำให้ Stop Loss กว้างเกินความจำเป็น'
      },
      {
        id: 'lesson-3-2',
        title: '4 รูปแบบโครงสร้างโซน & วิธีตีกรอบโซนที่ถูกต้อง',
        content: `ในหน้า 14-18 ของ E-Book ได้จำแนกโซนออกเป็น 4 รูปแบบชัดเจน:

**Demand (โซนซื้อ) 2 รูปแบบ:**
1. **Drop Base Rally (DBR) (หน้า 14):** ราคาปรับตัวลงมา (Drop) -> พักตัวเป็นกลุ่ม (Base) -> มีแรงซื้อดันราคาพุ่งขึ้นอย่างรวดเร็ว (Rally) นิยมใช้เล่นจังหวะ Reversal
2. **Rally Base Rally (RBR) (หน้า 15):** ราคามีการปรับตัวขึ้น (Rally) -> พักตัวสั้นๆ (Base) -> ปรับตัวขึ้นต่อ (Rally) นิยมใช้เล่นตามเทรน (Trend Continuation)

**Supply (โซนขาย) 2 รูปแบบ:**
1. **Rally Base Drop (RBD) (หน้า 16):** ราคาวิ่งขึ้นมา (Rally) -> พักตัวเป็นกลุ่ม (Base) -> ปรับตัวลงรุนแรง (Drop)
2. **Drop Base Drop (DBD) (หน้า 17):** ราคาดันตัวลงไป (Drop) -> พักตัวเป็นกลุ่ม (Base) -> ทิ้งตัวลงต่อไป (Drop)

**วิธีการตีกรอบโซนที่ถูกต้อง (หน้า 18):**
เราจะเลือกส่วนที่มีการ **Base หรือออกข้าง รวมถึง "ไส้เทียน" (ทั้ง High และ Low ของแท่ง Base)** เป็นกรอบ Demand & Supply Zone เพื่อไม่ให้ราคาเกี่ยวไส้เทียนหลุดออกไป`,
        corePrinciples: [
          'DBR และ RBD เป็นโซนกลับตัว (Reversal Zones)',
          'RBR และ DBD เป็นโซนตามแนวโน้มเดิม (Continuation Zones)',
          'การตีกรอบต้องคลุมทั้งเนื้อเทียนและไส้เทียนของแท่ง Base'
        ],
        practicalExamples: 'ในกราฟทองคำ XAUUSD แท่งเทียนทิ้งตัวลงมาที่ 2300 พักตัวเป็นแท่ง Doji เล็กๆ แล้วดีดตัวขึ้นไป 2350 ทันที เมื่อราคาย้อนกลับมาที่ 2300 โซน DBR นี้จะทำหน้าที่เป็นแนวรับดีดราคากลับขึ้นไป',
        proTips: 'โซนที่เพิ่งสร้างสดใหม่และยังไม่เคยถูกทดสอบ (Fresh Zone) จะมีโอกาสชนะสูงกว่าโซนที่ถูกทดสอบไปแล้วหลายครั้ง',
        pitfalls: 'ตีกรอบเฉพาะเนื้อเทียนแล้วปล่อยให้ไส้เทียนอยู่นอกโซน ทำให้ถูก Stop Out ได้ง่ายเมื่อราคากวาดไส้'
      }
    ],
    quiz: [
      {
        id: 'q3-1',
        type: 'mcq',
        question: 'รูปแบบใดต่อไปนี้จัดเป็น Demand รูปแบบกลับตัว (Reversal Demand) ตามหน้า 14 ของ E-Book?',
        options: [
          'Rally Base Rally (RBR)',
          'Drop Base Rally (DBR)',
          'Drop Base Drop (DBD)',
          'Rally Base Drop (RBD)'
        ],
        correctIndex: 1,
        explanation: 'หน้า 14 ระบุว่า Drop Base Rally (DBR) คือราคาปรับตัวลงมา (Drop) พักตัวเป็นกลุ่ม (Base) แล้วมีแรงซื้อดันราคาปรับตัวขึ้นอย่างรวดเร็ว (Rally)',
        referenceConcept: 'E-Book หน้า 14: DBR Demand Pattern'
      },
      {
        id: 'q3-2',
        type: 'mcq',
        question: 'ตามหน้า 18 ของ E-Book วิธีการตีกรอบ Demand & Supply Zone ที่ถูกต้องคือข้อใด?',
        options: [
          'เลือกเฉพาะเนื้อเทียน ห้ามรวมไส้เทียน',
          'เลือกส่วนที่มีการ Base ออกข้าง รวมถึงไส้เทียน เป็นกรอบโซน',
          'ลากเส้นแนวนอนเส้นเดียวที่ราคาปิด',
          'ตีกรอบคลุมทั้งสวิง High ถึง Low ใหญ่'
        ],
        correctIndex: 1,
        explanation: 'หน้า 18 ระบุว่า "โดยเราจะเลือกส่วนที่มีการ Base หรือออกข้าง รวมถึงไส้เทียน เป็นกรอบ Demand & Supply Zone"',
        referenceConcept: 'E-Book หน้า 18: การตีกรอบโซน'
      }
    ]
  },
  {
    id: 'ch-04-impulse-pullback',
    chapterNumber: 4,
    title: 'Impulse Wave & Pullback Wave (คลื่นส่งและคลื่นพักตัว)',
    englishTitle: 'Impulse vs Pullback Waves Mechanics',
    category: 'Structure',
    difficulty: 'Beginner',
    estimatedMinutes: 15,
    pdfPages: '19 - 24',
    shortDescription: 'แยกแยะความแตกต่างระหว่างคลื่นส่งหลักของสถาบัน (Impulse) กับคลื่นพักตัวของรายย่อย (Pullback)',
    whyItMatters: 'หากคุณเข้าออเดอร์ใน Pullback Wave ที่ยังไม่จบ คุณจะติดดอยทันที ต้องแยกให้ออกว่าคลื่นไหนคือแรงจริง',
    summary: [
      'Impulse Wave คือ คลื่นขยายหรือคลื่นส่งหลักของเทรน เคลื่อนที่รุนแรงและรวดเร็ว',
      'Pullback Wave คือ คลื่นย่อยที่เป็นการพักราคา สวนทางกับเทรนหลัก',
      'ใน Up Trend: คลื่นพุ่งขึ้นคือ Impulse และคลื่นย่อลงคือ Pullback',
      'ใน Down Trend: คลื่นทิ้งตัวลงคือ Impulse และคลื่นเด้งขึ้นคือ Pullback'
    ],
    keyTerms: [
      { term: 'Impulse Wave', meaning: 'คลื่นส่งหลักที่มีโมเมนตัมแข็งแกร่ง เกิดจากการเข้าทำของ Smart Money' },
      { term: 'Pullback Wave', meaning: 'คลื่นพักตัวสั้นๆ สวนทางกับเทรนหลัก มีขนาดแท่งเทียนเล็กและเคลื่อนที่ช้า' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_019.png',
        caption: 'หน้า 19: นิยาม Impulse Wave คือคลื่นขยายคลื่นส่งหลักของเทรน',
        page: 19
      },
      {
        url: '/extracted/page_renders/page_020.png',
        caption: 'หน้า 20: Impulse Wave ใน Up trend และ Down trend',
        page: 20
      },
      {
        url: '/extracted/page_renders/page_021.png',
        caption: 'หน้า 21: นิยาม Pullback Wave คือคลื่นย่อยเป็นการพักราคา',
        page: 21
      },
      {
        url: '/extracted/page_renders/page_022.png',
        caption: 'หน้า 22: Pullback Wave ใน Up trend และ Down trend',
        page: 22
      },
      {
        url: '/extracted/page_renders/page_023.png',
        caption: 'หน้า 23-24: การผสมผสานระหว่าง Impulse Wave & Pullback Wave ในรอบวัฏจักรราคา',
        page: 23
      }
    ],
    lessons: [
      {
        id: 'lesson-4-1',
        title: 'ลักษณะเฉพาะของ Impulse vs Pullback',
        content: `จากหน้า 19-24 ของ E-Book:

**1. Impulse Wave (คลื่นส่งหลัก):**
- เป็นคลื่นที่เดินทางตามแนวโน้มหลักของตลาด
- แท่งเทียนมักมีขนาดใหญ่ เนื้อเทียนแน่น ไส้เทียนสั้น
- มีความชันสูง ใช้เวลาน้อยแต่เคลื่อนที่ได้ระยะทางไกล
- เกิดขึ้นเมื่อ Smart Money อัดฉีดสภาพคล่องและกวาดออเดอร์ในตลาด

**2. Pullback Wave (คลื่นพักตัว):**
- เป็นคลื่นที่เคลื่อนที่สวนทางกับแนวโน้มหลัก
- แท่งเทียนมักมีขนาดเล็ก ซ้อนทับกัน (Overlapping) มีไส้เทียนเยอะ
- ความชันต่ำ ใช้เวลาเดินทางนานแต่ได้ระยะทางสั้น
- เป็นช่วงที่รายย่อยเข้ามาพยายามสวนเทรน หรือ Smart Money ปิดกำไรบางส่วนเพื่อดักสภาพคล่อง`,
        corePrinciples: [
          'เราเทรด "ตามทิศทางของ Impulse Wave" เสมอ',
          'เราจะรอให้ Pullback Wave จบลงที่โซนสำคัญ แล้วเข้าออเดอร์เพื่อขี่คลื่น Impulse ลูกถัดไป',
          'อย่าพยายามดักเทรดเก็บเศษเงินใน Pullback Wave เพราะเสี่ยงต่อการถูก Impulse ดันทะลุ'
        ],
        practicalExamples: 'ในเทรนขาขึ้น แท่งเขียว 3 แท่งพุ่งขึ้น 100 จุด (Impulse) จากนั้นราคาค่อยๆ ย่อลงด้วยแท่งแดงเล็กๆ 8 แท่ง ลงมาเพียง 30 จุด (Pullback) นี่คือจังหวะที่ต้องเตรียม Buy ไม่ใช่เตรียม Sell',
        proTips: 'เปรียบเทียบจำนวนแท่งเทียน: ถ้าขึ้น 3 แท่งแต่ลง 10 แท่ง แปลว่าแรงซื้อยังได้เปรียบมหาศาล',
        pitfalls: 'เห็นแท่งแดงในขาขึ้นแล้วตกใจคิดว่าเทรนเปลี่ยน ทั้งๆ ที่เป็นแค่การพักตัวแบบ Pullback'
      }
    ],
    quiz: [
      {
        id: 'q4-1',
        type: 'mcq',
        question: 'ตามหน้า 19 และ 21 ของ E-Book ข้อใดอธิบายความแตกต่างของ Impulse Wave และ Pullback Wave ได้ถูกต้องที่สุด?',
        options: [
          'Impulse คือคลื่นพักตัวช้าๆ ส่วน Pullback คือคลื่นส่งหลักที่พุ่งเร็ว',
          'Impulse คือคลื่นขยายคลื่นส่งหลักของเทรน ส่วน Pullback คือคลื่นย่อยที่เป็นการพักราคา',
          'ทั้งสองคลื่นมีขนาดและความเร็วเท่ากันทุกประการ',
          'Impulse เกิดเฉพาะในขาลง ส่วน Pullback เกิดเฉพาะในขาขึ้น'
        ],
        correctIndex: 1,
        explanation: 'หน้า 19 ระบุว่า Impulse คือคลื่นขยายคลื่นส่งหลัก และหน้า 21 ระบุว่า Pullback คือคลื่นย่อยเป็นการพักราคา',
        referenceConcept: 'E-Book หน้า 19-22: Wave Mechanics'
      }
    ]
  },
  {
    id: 'ch-05-valid-pullback',
    chapterNumber: 5,
    title: 'Valid Pullback (Advance) (การพักราคาที่ถูกต้อง)',
    englishTitle: 'Valid Pullback: Exact Candle Sweep Conditions',
    category: 'Structure',
    difficulty: 'Intermediate',
    estimatedMinutes: 25,
    pdfPages: '25 - 28',
    shortDescription: 'กฎเหล็กแท่งเทียนในการระบุ Valid Pullback ที่ถูกต้อง ห้ามเดาสวิงด้วยสายตา!',
    whyItMatters: 'นี่คือบันไดขั้นแรกสุดของระบบ SMC ทั้งหมด หากระบุ Valid Pullback ไม่เป็น คุณจะหา IDM, BOS และ CHoCH ผิดทั้งหมด!',
    summary: [
      'Valid Pullback คือสวิงหรือการพักราคาที่ถูกต้องตามเงื่อนไขของแท่งเทียน',
      'ใน Up Trend: ต้องเกิดแท่งที่สูงที่สุดของโมเมนตัม และต้องถูกแท่งถัดๆ ไป "เบรค/กวาด Low" ของแท่งสูงสุดนั้นให้ได้',
      'หากแท่งถัดไปไม่สามารถเบรค Low ของแท่งสูงสุดได้ จะถือว่าเป็น Inside Bar ไม่ใช่ Valid Pullback',
      'ใน Down Trend: ต้องเกิดแท่งที่ต่ำที่สุดของโมเมนตัม และต้องถูกแท่งถัดๆ ไป "เบรค/กวาด High" ของแท่งต่ำสุดนั้นให้ได้'
    ],
    keyTerms: [
      { term: 'Valid Pullback', meaning: 'การพักราคาที่แท่งเทียนถัดไปกวาด High หรือ Low ของแท่งสูงสุด/ต่ำสุดของรอบ' },
      { term: 'Highest Candle', meaning: 'แท่งเทียนที่ทำราคาสูงสุดของรอบโมเมนตัมนั้นๆ' },
      { term: 'Lowest Candle', meaning: 'แท่งเทียนที่ทำราคาต่ำสุดของรอบโมเมนตัมนั้นๆ' },
      { term: 'Inside Bar', meaning: 'แท่งเทียนที่เคลื่อนไหวอยู่ภายในกรอบ High และ Low ของแท่งแม่ ไม่นับเป็นสวิงใหม่' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_025.png',
        caption: 'หน้า 25: เงื่อนไขการเกิด Valid Pullback ใน Up Trend',
        page: 25
      },
      {
        url: '/extracted/page_renders/page_026.png',
        caption: 'หน้า 26: แผนภาพแท่งเทียน Valid Pullback ใน Up Trend',
        page: 26
      },
      {
        url: '/extracted/page_renders/page_027.png',
        caption: 'หน้า 27: เงื่อนไขการเกิด Valid Pullback ใน Down Trend',
        page: 27
      },
      {
        url: '/extracted/page_renders/page_028.png',
        caption: 'หน้า 28: แผนภาพแท่งเทียน Valid Pullback ใน Down Trend',
        page: 28
      }
    ],
    lessons: [
      {
        id: 'lesson-5-1',
        title: 'เงื่อนไข Valid Pullback ในเทรนขาขึ้น (Up Trend)',
        content: `ในหน้า 25-26 ของ E-Book ได้กำหนดเงื่อนไขทางคณิตศาสตร์แท่งเทียนไว้ชัดเจน:

**เงื่อนไขใน Up Trend (หน้า 25):**
1. กราฟได้ทำแท่งที่ **"สูงที่สุดของโมเมนตัม" (Highest Candle)**
2. ต้องถูกแท่งถัดๆ ไป **"เบรค Low ของแท่งที่สูงที่สุด"**
3. หากแท่งถัดไปไม่สามารถทำลาย Low ของแท่งสูงสุดได้ (ราคาวิ่งอยู่ในช่วง High-Low ของแท่งสูงสุด) เราจะถือว่าเป็น Inside Bar ไม่นับเป็นการพักตัว
4. การเบรค Low ของแท่งสูงสุดนี้ **ใช้เพียงแค่ "ไส้เทียน" (Wick) กวาดผ่านก็ถือว่า Valid แล้ว!** (ไม่จำเป็นต้องรอเนื้อเทียนปิดใต้ Low สำหรับการทำ Pullback)

**ทำไมกฎนี้ถึงสำคัญ?**
เพราะการที่แท่งถัดไปหลุด Low ของแท่งสูงสุด เป็นสัญญาณแรกทางโครงสร้างว่า มีแรงขายเข้ามาดึงสภาพคล่องย่อยแล้ว จึงนับเป็นจุดเริ่มต้นของการพักตัว`,
        corePrinciples: [
          'หาแท่งที่ High สูงที่สุดในรอบโมเมนตัมให้เจอ',
          'ดูว่าแท่งถัดไปมีแท่งไหนที่หลุด Low ของแท่งสูงสุดนั้นหรือไม่',
          'ถ้าหลุด Low -> นับเป็น Valid Pullback ทันที',
          'ถ้าไม่หลุด Low แต่ดันทำ High ใหม่ -> ให้ย้ายแท่งอ้างอิงไปยังแท่งใหม่ที่สูงกว่า'
        ],
        practicalExamples: 'แท่งที่ 1 มี High 100, Low 80 แท่งที่ 2 มี High 95, Low 78 แท่งที่ 2 ได้กวาด Low 80 ของแท่งที่ 1 สำเร็จ จึงนับว่าเกิด Valid Pullback แล้ว',
        proTips: 'อย่ามองแค่เส้นกราฟิกซิกแซก ให้ซูมดูที่ระดับแท่งเทียนจริงเสมอ เพราะความแม่นยำของ SMC อยู่ที่จุดกวาดของไส้เทียน',
        pitfalls: 'นับแท่งสีแดงว่าเป็น Pullback เสมอ ทั้งที่แท่งแดงนั้นยังไม่เคยหลุด Low ของแท่งสูงสุดเลย'
      },
      {
        id: 'lesson-5-2',
        title: 'เงื่อนไข Valid Pullback ในเทรนขาลง (Down Trend)',
        content: `ในหน้า 27-28 ของ E-Book ระบุเงื่อนไขใน Down Trend ในลักษณะสมมาตร:

**เงื่อนไขใน Down Trend (หน้า 27):**
1. กราฟได้ทำแท่งที่ **"ต่ำที่สุดของโมเมนตัม" (Lowest Candle)**
2. ต้องถูกแท่งถัดๆ ไป **"เบรค High ของแท่งที่ต่ำที่สุด"**
3. มีการเบรค High ของแท่งต่ำสุด (ใช้ไส้เทียนกวาดผ่านก็นับ)
4. เมื่อเบรค High สำเร็จ จึงจะยืนยันว่าเกิด Valid Pullback ของฝั่งขาลง`,
        corePrinciples: [
          'หาแท่งที่ Low ต่ำที่สุดในคลื่นขาลง',
          'แท่งถัดไปต้องกวาด High ของแท่งต่ำสุดนั้น',
          'หากแท่งถัดไปยังทำ New Low ต่อไปเรื่อยๆ ให้ย้ายแท่งอ้างอิงตามลงไปจนกว่าจะมีการกวาด High'
        ],
        practicalExamples: 'แท่งที่ 1 มี High 50, Low 30 แท่งที่ 2 มี High 52, Low 32 แท่งที่ 2 ดีดตัวขึ้นไปกิน High 50 ของแท่งที่ 1 สำเร็จ จึงเกิด Valid Pullback ฝั่งขาลง',
        proTips: 'จุดที่เกิด Valid Pullback ในขาลงนี้เอง ที่จะทำหน้าที่เป็นจุด IDM (Inducement) ให้เราในบทถัดไป',
        pitfalls: 'เข้าใจผิดว่าการเด้งขึ้นต้องปิดเนื้อเทียนเหนือ High แท้จริงแล้วแค่ไส้เทียนสะกิดกิน High ก็นับเป็น Valid Pullback แล้ว'
      }
    ],
    quiz: [
      {
        id: 'q5-1',
        type: 'scenario',
        question: 'ในเทรนขาขึ้น แท่ง A ทำจุดสูงสุด High ที่ 2000 และ Low ที่ 1980 แท่ง B ถัดมาทำ High ที่ 1995 และ Low ที่ 1985 (ไม่หลุด 1980) จากนั้นแท่ง C ทำ High ที่ 2010 กรณีนี้เกิด Valid Pullback ที่แท่ง A หรือไม่?',
        options: [
          'เกิด Valid Pullback เพราะแท่ง B เป็นแท่งสีแดง',
          'ไม่เกิด Valid Pullback เพราะแท่ง B ไม่สามารถเบรค Low 1980 ของแท่ง A ได้ และแท่ง C พุ่งทำ High ใหม่',
          'เกิด Valid Pullback เพราะราคาย่อตัวลงมา',
          'ขึ้นอยู่กับ Timeframe ที่ดู'
        ],
        correctIndex: 1,
        explanation: 'ตามหน้า 25 ของ E-Book เงื่อนไข Valid Pullback ใน Up Trend คือต้องถูกแท่งถัดๆ ไปเบรค Low ของแท่งที่สูงที่สุด เมื่อแท่ง B ไม่หลุด Low และแท่ง C ทำ High ใหม่ จุดอ้างอิงสูงสุดจึงย้ายไปที่แท่ง C แทน จึงไม่เคยเกิด Valid Pullback ขึ้นเลย',
        referenceConcept: 'E-Book หน้า 25: Valid Pullback Up Trend'
      },
      {
        id: 'q5-2',
        type: 'tf',
        question: 'การเบรค High หรือ Low เพื่อยืนยัน Valid Pullback จำเป็นต้องรอให้เนื้อเทียนปิดทะลุหรือไม่ หรือใช้เพียงไส้เทียนกวาดผ่านก็เพียงพอ?',
        options: [
          'ใช้เพียงไส้เทียนกวาดผ่าน (Sweep) ก็ถือว่าเป็น Valid Pullback แล้ว',
          'ต้องรอให้เนื้อเทียนปิดทะลุเท่านั้นจึงจะนับ'
        ],
        correctIndex: 0,
        explanation: 'ในการระบุ Valid Pullback ขอเพียงแค่มีไส้เทียนของแท่งถัดไปกวาดผ่าน High หรือ Low ของแท่งอ้างอิง ก็ถือว่าเป็นการพักราคาที่ถูกต้องแล้ว ต่างจาก BOS ที่ต้องใช้เนื้อเทียน',
        referenceConcept: 'E-Book หน้า 25-28: กฎแท่งเทียน Valid Pullback'
      }
    ]
  },
  {
    id: 'ch-06-bos-break-of-structure',
    chapterNumber: 6,
    title: 'BOS : Break of Structure (Advance) (การเบรคโครงสร้าง)',
    englishTitle: 'BOS Mechanics: Body Close vs Wick Transfer',
    category: 'Structure',
    difficulty: 'Intermediate',
    estimatedMinutes: 20,
    pdfPages: '29 - 32',
    shortDescription: 'กฎเหล็กของ BOS: ต้องเบรคด้วยเนื้อเทียนเท่านั้น! และปรากฏการณ์การย้ายจุด High/Low เมื่อเบรคด้วยไส้',
    whyItMatters: 'มือใหม่ 90% โดนหลอกเพราะเห็นไส้เทียนแหย่ทะลุแล้วคิดว่าเบรคแล้ว จึงโดน Fakeout ลากไปกิน SL ทันที',
    summary: [
      'BOS (Break of Structure) คือ การที่ราคาเป็นเทรน และเบรค High เดิมไปสร้าง High ใหม่ หรือเบรค Low เดิมไปสร้าง Low ใหม่',
      'กฎเหล็กข้อ 1 (หน้า 30): BOS ที่ถูกต้อง "ต้องถูกเบรคด้วยเนื้อเทียน" (Body Close) เท่านั้น!',
      'กฎเหล็กข้อ 2 (หน้า 31): หากเบรคด้วยไส้เทียน จุด High/Low จะถูก "เคลื่อนย้าย (Transfer)" ไปยังปลายไส้ จนกว่าจะมีการเบรคด้วยเนื้อเทียน',
      'กฎเหล็กข้อ 3 (หน้า 32): หากราคาหลุด Low โดยที่ยังไม่เกิด BOS ที่ถูกต้อง CHoCH ที่เกิดขึ้นก็จะไม่ใช่ CHoCH ที่แท้จริง (Fake Reversal)'
    ],
    keyTerms: [
      { term: 'BOS (Break of Structure)', meaning: 'การทะลุโครงสร้างตามแนวโน้มเดิมเพื่อยืนยันการไปต่อของเทรน' },
      { term: 'Candle Body Break', meaning: 'การที่เนื้อเทียนปิดเหนือหรือใต้ระดับสำคัญอย่างสมบูรณ์' },
      { term: 'Wick Break / Sweep', meaning: 'การที่ราคาใช้เพียงไส้เทียนแหย่ทะลุ แต่เนื้อเทียนปิดถอยกลับมา' },
      { term: 'High/Low Transfer', meaning: 'การเลื่อนตำแหน่งจุด High หรือ Low ไปตามปลายไส้เทียนใหม่ที่ทำสถิติ' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_029.png',
        caption: 'หน้า 29: นิยาม BOS Break of Structure',
        page: 29
      },
      {
        url: '/extracted/page_renders/page_030.png',
        caption: 'หน้า 30: กฎเหล็ก BOS ที่ถูกต้อง ต้องถูกเบรคด้วยเนื้อเทียน',
        page: 30
      },
      {
        url: '/extracted/page_renders/page_031.png',
        caption: 'หน้า 31: การเบรคด้วยไส้เทียน HH จะถูกเคลื่อนย้ายไปยังปลายไส้เทียน',
        page: 31
      },
      {
        url: '/extracted/page_renders/page_032.png',
        caption: 'หน้า 32: กราฟเบรค Low โดยยังไม่ทำ BOS ที่ถูกต้อง CHoCH จะไม่ใช่ของจริง',
        page: 32
      }
    ],
    lessons: [
      {
        id: 'lesson-6-1',
        title: 'BOS ที่ถูกต้อง: เนื้อเทียน vs ไส้เทียน (Candle Body vs Wick)',
        content: `จากหน้า 29-31 ของ E-Book:

**1. นิยาม BOS (หน้า 29):**
BOS คือการที่ราคาเดินทางในเทรนเดิม แล้วมีแรงผลักดันทะลุ High เดิม (ในขาขึ้น) หรือทะลุ Low เดิม (ในขาลง) เป็นการยืนยันว่าแนวโน้มเดิมยังมีพลังที่จะไปต่อ

**2. กฎเนื้อเทียน (หน้า 30):**
**"BOS ที่ถูกต้อง ต้องถูกเบรคด้วยเนื้อเทียน"**
หากแท่งเทียนพุ่งขึ้นไปเหนือ High เดิม แต่เมื่อจบแท่ง (Candle Close) เนื้อเทียนกลับปิดต่ำกว่าเส้น High เดิม เหลือทิ้งไว้เพียงไส้เทียนยาวๆ ด้านบน **เราจะไม่นับว่าเกิด BOS!**

**3. การย้ายจุด High (High Transfer) (หน้า 31):**
ในกรณีที่ราคาเบรคด้วยไส้เทียน:
- จุด Higher High (HH) จะถูก **"เคลื่อนย้าย"** ไปยังบริเวณปลายไส้เทียนสูงสุดแท่งนั้น
- และเราจะต้องรอจนกว่าจะมีแท่งเทียนถัดไปสามารถ **ปิดเนื้อเทียน** เหนือปลายไส้ใหม่นั้นได้ จึงจะถือว่าเกิด BOS ที่สมบูรณ์!`,
        corePrinciples: [
          'BOS ต้องปิดด้วยเนื้อเทียนเท่านั้น',
          'ไส้เทียนที่แหย่ทะลุ คือการ Liquidity Sweep ไม่ใช่ BOS',
          'เมื่อเกิดไส้ทะลุ ให้เลื่อนระดับ High ไปที่ปลายไส้ใหม่ทันที'
        ],
        practicalExamples: 'ราคา High เดิมอยู่ที่ 100 มีแท่งเทียนแทงไส้ขึ้นไป 105 แต่ปิดเนื้อที่ 98 จุด High ใหม่จะเลื่อนเป็น 105 ทันที จนกระทั่งแท่งถัดไปปิดเนื้อเทียนที่ 106 จึงจะเกิด BOS ที่ถูกต้อง',
        proTips: 'อย่าเพิ่งรีบขีดเส้น BOS ขณะที่แท่งเทียนยังไม่ปิด รอให้เวลานับถอยหลังของแท่งเทียนจบลงก่อนเสมอ',
        pitfalls: 'เข้า Buy ทันทีที่เห็นราคาแลบทะลุ High ระหว่างแท่ง แล้วถูกดึงไส้กลับกลายเป็นติดดอย'
      },
      {
        id: 'lesson-6-2',
        title: 'ผลกระทบต่อ CHoCH เมื่อ BOS ยังไม่สมบูรณ์',
        content: `ในหน้า 32 ของ E-Book มีคำเตือนระดับทองคำ:
**"ถ้าหากกราฟถูกเบรค Low โดยที่กราฟยังไม่ทำ BOS ที่ถูกต้อง CHoCH ก็จะไม่ใช่ CHoCH ที่แท้จริงเช่นกัน"**

**ความหมายเชิงลึก:**
หากราคายังไม่เคยยืนยันการทำ BOS (เช่น ทำได้แค่แลบไส้) แล้วจู่ๆ ราคาร่วงลงมาหลุด Low ก่อนหน้า เทรดเดอร์ทั่วไปจะตื่นตระหนกว่าเกิด CHoCH (กลับตัวเป็นขาลง) แล้วรีบเปิด Sell
แต่ในความเป็นจริง โครงสร้างขาขึ้นยังไม่สมบูรณ์ การหลุด Low ครั้งนี้มักเป็นเพียงการกวาดสภาพคล่อง (Liquidity Sweep) เพื่อพุ่งขึ้นต่อ!`,
        corePrinciples: [
          'CHoCH ที่แท้จริงจะเกิดขึ้นได้ ก็ต่อเมื่อสวิงก่อนหน้าทำ BOS ที่สมบูรณ์แล้วเท่านั้น',
          'หากยังไม่ BOS การหลุด Low ไม่ใช่การกลับตัว แต่เป็นกับดักสภาพคล่อง'
        ],
        practicalExamples: 'กราฟแลบไส้เหนือ High แล้วร่วงหลุด Low ย่อย รายย่อยคิดว่า CHoCH จึงเปิด Sell แต่สถาบันดึงกราฟกลับพุ่งขึ้นทำลายฝั่ง Sell ทั้งหมด',
        proTips: 'ตรวจสอบประวัติของสวิง High ก่อนหน้าเสมอว่าได้รับการยืนยันด้วยเนื้อเทียนแล้วหรือยังก่อนจะพิจารณาจุด CHoCH',
        pitfalls: 'เทรดสวนทางเทรนใหญ่เพราะหลงเชื่อ CHoCH หลอกที่เกิดจาก BOS ไม่สมบูรณ์'
      }
    ],
    quiz: [
      {
        id: 'q6-1',
        type: 'mcq',
        question: 'ตามหน้า 30-31 ของ E-Book หากแท่งเทียนพุ่งทะลุ High เดิมด้วย "ไส้เทียน" แต่เนื้อเทียนปิดต่ำกว่า High เดิม จะเกิดอะไรขึ้น?',
        options: [
          'นับเป็น BOS ที่สมบูรณ์ทันทีและเทรนไปต่อ',
          'เกิดการกลับตัวเป็นขาลงทันที',
          'ไม่นับเป็น BOS แต่จุด HH จะถูกเคลื่อนย้ายไปยังปลายไส้เทียนนั้น จนกว่าจะมีแท่งปิดเนื้อเทียนทะลุได้',
          'ถือว่าตลาดเข้าสู่สภาวะ Side ways'
        ],
        correctIndex: 2,
        explanation: 'หน้า 31 ระบุว่า "ลักษณะการที่เบรค BOS ด้วยใส้เทียน HH จะถูกเคลื่อนย้ายไปยังบริเวณที่ถูกใส้เทียนเบรค จนกว่าจะมีการเบรคด้วยเนื้อเทียน"',
        referenceConcept: 'E-Book หน้า 30-31: กฎการเบรค BOS'
      },
      {
        id: 'q6-2',
        type: 'tf',
        question: 'หากราคาวิ่งหลุด Low ลงมา โดยที่สวิงด้านบนยังไม่เคยเกิด BOS ที่ถูกต้อง จุดที่หลุดนั้นถือเป็น CHoCH ที่แท้จริงหรือไม่?',
        options: [
          'ไม่ใช่ CHoCH ที่แท้จริง (ตามคำเตือนหน้า 32)',
          'ใช่ เป็น CHoCH ที่แท้จริงแน่นอนเพราะหลุด Low แล้ว'
        ],
        correctIndex: 0,
        explanation: 'หน้า 32 ของ E-Book ระบุว่า "ถ้าหากกราฟถูกเบรคโลว์โดยที่กราฟยังไม่ทำ BOS ที่ถูกต้อง CHoCH ก็จะไม่ใช่ CHoCH ที่แท้จริงเช่นกัน"',
        referenceConcept: 'E-Book หน้า 32: ความสัมพันธ์ระหว่าง BOS และ CHoCH'
      }
    ]
  },
  {
    id: 'ch-07-idm-inducement',
    chapterNumber: 7,
    title: 'IDM : Inducement (Advance) (กับดักการล่อซื้อขาย)',
    englishTitle: 'Inducement: Swing Confirmation & Retail Traps',
    category: 'Liquidity',
    difficulty: 'Advanced',
    estimatedMinutes: 35,
    pdfPages: '33 - 52',
    shortDescription: 'หัวใจสำคัญที่สุดของ SMC: IDM คืออะไร ทำไมต้องรอให้เคลียร์ IDM ก่อนจึงจะคอนเฟิร์ม High หรือ Low ที่แท้จริง',
    whyItMatters: 'หากคุณไม่เข้าใจ IDM คุณจะเข้าเทรดที่จุดที่ Smart Money ใช้เป็นเหยื่อล่อ และกลายเป็นสภาพคล่องให้สถาบันกิน',
    summary: [
      'IDM (Inducement) คือสวิง Valid Pullback แรกที่อยู่ใกล้โมเมนตัมปัจจุบันที่สุด',
      'ใน Up Trend: จุดสูงสุด (High) จะได้รับการ "คอนเฟิร์ม" ก็ต่อเมื่อราคาถอยกลับมา "เคลียร์ IDM" ได้สำเร็จเท่านั้น!',
      'ใน Down Trend: จุดต่ำสุด (Low) จะได้รับการ "คอนเฟิร์ม" ก็ต่อเมื่อราคาดีดตัวกลับมา "เคลียร์ IDM" ได้สำเร็จเท่านั้น!',
      'หากราคาไม่เกิด Valid Pullback ที่ถูกต้อง จุดนั้นจะไม่นับเป็น IDM',
      'หากมีหลายสวิง ให้ใช้ IDM ตัวแรกสุด (Valid Pullback แรกสุด) ในการคอนเฟิร์ม High หรือ Low'
    ],
    keyTerms: [
      { term: 'IDM (Inducement)', meaning: 'จุดล่อสภาพคล่องย่อยที่ Smart Money สร้างขึ้นเพื่อล่อให้รายย่อยเข้าเทรดก่อนเวลา' },
      { term: 'Confirm High', meaning: 'การยืนยันว่าจุดสูงสุดนั้นคือ Higher High ที่แท้จริง เกิดขึ้นเมื่อราคาถอยมากวาด IDM' },
      { term: 'Confirm Low', meaning: 'การยืนยันว่าจุดต่ำสุดนั้นคือ Lower Low ที่แท้จริง เกิดขึ้นเมื่อราคาดีดตัวมากวาด IDM' },
      { term: 'Sweep IDM', meaning: 'การที่ราคาวิ่งย้อนกลับมากวาดกินสภาพคล่องที่จุด IDM' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_033.png',
        caption: 'หน้า 33: นิยาม IDM Inducement คือสวิง Valid Pullback',
        page: 33
      },
      {
        url: '/extracted/page_renders/page_034.png',
        caption: 'หน้า 34: จุดต่ำสุดของโมเมนตัมกลายเป็น IDM ใน Up Trend',
        page: 34
      },
      {
        url: '/extracted/page_renders/page_037.png',
        caption: 'หน้า 37: IDM ใน Down Trend จุดสูงสุดของโมเมนตัมกลายเป็น IDM',
        page: 37
      },
      {
        url: '/extracted/page_renders/page_039.png',
        caption: 'หน้า 39: การใช้ IDM คอนเฟิร์ม HIGH และ LOW เมื่อถูกเคลียร์',
        page: 39
      },
      {
        url: '/extracted/page_renders/page_044.png',
        caption: 'หน้า 44: เมื่อมีการเคลียร์ IDM แล้วเราจึงคอนเฟิร์ม Low ใน Down Trend',
        page: 44
      },
      {
        url: '/extracted/page_renders/page_048.png',
        caption: 'หน้า 48: IDM เชิงลึกจากแท่งเทียนและการย้ายตำแหน่ง BOS ที่ไม่สมบูรณ์',
        page: 48
      }
    ],
    lessons: [
      {
        id: 'lesson-7-1',
        title: 'นิยามของ IDM และการกำเนิดจาก Valid Pullback',
        content: `จากหน้า 33-38 ของ E-Book:

**IDM (Inducement) คืออะไร?**
IDM แปลตรงตัวว่า "สิ่งล่อใจ" หรือ "กับดักล่อซื้อขาย"
ในทางเทคนิค SMC **"IDM คือสวิงที่ถูกต้อง หรือก็คือ Valid Pullback แรกที่เกิดขึ้นในเทรน"**

**เงื่อนไขการเกิด IDM:**
1. ใน Up Trend (หน้า 34): เมื่อราคาวิ่งขึ้นไปทำยอดสูงสุด แล้วเกิด Valid Pullback ย่อตัวลงมา **จุดต่ำสุดของสวิง Valid Pullback นั้นจะกลายเป็นจุด IDM ทันที!**
2. ใน Down Trend (หน้า 37): เมื่อราคาทิ้งตัวลงไปทำจุดต่ำสุด แล้วเกิด Valid Pullback ดีดตัวขึ้นมา **จุดสูงสุดของสวิง Valid Pullback นั้นจะกลายเป็นจุด IDM ทันที!**
3. กฎเหล็ก (หน้า 35 & 38): **"หากไม่เกิดการสร้าง Valid Pullback ที่ถูกต้อง ก็จะยังไม่ใช่ IDM เช่นกัน"**`,
        corePrinciples: [
          'IDM ต้องเป็น Valid Pullback ที่ถูกต้องตามกฎแท่งเทียนเท่านั้น',
          'สวิงหลอกที่ไม่กวาด High/Low จะไม่นับเป็น IDM',
          'IDM คือจุดที่รายย่อยมักเข้าใจผิดว่าเป็นแนวรับแนวต้านแล้วตั้ง Stop Loss ไว้'
        ],
        practicalExamples: 'ในขาขึ้น ราคาสร้าง Valid Pullback ย่อลงมาที่ 100 แล้วพุ่งต่อไป 120 จุด 100 นั้นคือ IDM ทันที เมื่อราคาถอยลงมากิน 100 จุด High 120 จึงจะได้รับการคอนเฟิร์ม',
        proTips: 'อย่าเพิ่งลากเส้น High จนกว่าราคาจะย้อนกลับมากิน IDM แรก เพราะถ้าราคายังพุ่งต่อโดยไม่กิน IDM จุด High จะเลื่อนสูงขึ้นเรื่อยๆ',
        pitfalls: 'ตั้งคำสั่ง Buy ที่จุด IDM ทันที เพราะคิดว่าเป็นแนวรับ ทั้งที่ IDM ถูกสร้างขึ้นมาเพื่อให้ถูกชนทะลุ'
      },
      {
        id: 'lesson-7-2',
        title: 'การคอนเฟิร์ม HIGH และ LOW ด้วยการเคลียร์ IDM',
        content: `ในหน้า 39-44 ของ E-Book ตอบคำถามสำคัญที่สุดของเทรดเดอร์:
**"แล้วเราจะใช้ IDM ตัวไหนในการคอนเฟิร์ม HIGH, LOW ละ?"**

**กฎการคอนเฟิร์ม (หน้า 39):**
1. **เราจะใช้ IDM ในการคอนเฟิร์ม HIGH และ LOW และจะคอนเฟิร์มก็ต่อเมื่อ "IDM ถูกเคลียร์ (Swept/Taken)" แล้วเท่านั้น!**
2. โครงสร้างของเทรนจะสร้างสวิง Valid Pullback หรือ IDM ขึ้นมาเสมอ
3. **ใน Up Trend:** ตราบใดที่ราคายังไม่ถอยมากิน IDM ล่าสุด จุดยอดดอยด้านบนจะยัง "ไม่ได้รับการคอนเฟิร์มว่าเป็น Higher High" แต่เมื่อใดที่ราคากวาด IDM สำเร็จ ยอดสูงสุดก่อนหน้านั้นจะกลายเป็น **Confirmed High** ทันที!
4. **ใน Down Trend (หน้า 44):** เมื่อมีการเคลียร์ IDM ด้านบนแล้ว เราจึงจะ **คอนเฟิร์ม Low** ล่าสุดว่ามีตัวตนจริง!`,
        corePrinciples: [
          'High ในขาขึ้น ได้รับการคอนเฟิร์มเมื่อ IDM ถูกเคลียร์',
          'Low ในขาลง ได้รับการคอนเฟิร์มเมื่อ IDM ถูกเคลียร์',
          'การเคลียร์ IDM ใช้เพียงไส้เทียนกวาด (Sweep) ก็ถือว่าเคลียร์สำเร็จแล้ว'
        ],
        practicalExamples: 'ราคาทองคำทำยอดที่ 2400 ย่อตัวทำ Valid Pullback ที่ 2380 แล้ววิ่งขึ้นไป 2420 จุด IDM คือ 2380 ตราบใดที่ราคายังอยู่เหนือ 2380 ยอด 2420 ยังไม่คอนเฟิร์ม จนกระทั่งราคาทิ้งตัวลงมาแตะ 2379 จุด 2420 จึงได้รับการยืนยันว่าเป็น Higher High ที่แท้จริง!',
        proTips: 'เมื่อ High ได้รับการคอนเฟิร์มแล้ว นั่นแปลว่าเราได้กรอบสวิง (Trading Range) ที่สมบูรณ์ในการวางแผนเทรดรอบต่อไป',
        pitfalls: 'นับสวิง High ทันทีที่เห็นแท่งแดงย่อลงมา โดยไม่รอให้เกิดการกวาด IDM ทำให้ได้ระดับ Fibonacci และ POI ที่ผิดเพี้ยน'
      }
    ],
    quiz: [
      {
        id: 'q7-1',
        type: 'mcq',
        question: 'ตามหน้า 39 ของ E-Book จุด Higher High ในเทรนขาขึ้นจะได้รับการ "คอนเฟิร์ม" ว่าเป็น High ที่แท้จริงเมื่อใด?',
        options: [
          'เมื่อราคาปิดแท่งเขียวติดต่อกัน 5 แท่ง',
          'เมื่อราคาถอยกลับมา "เคลียร์ IDM" ได้สำเร็จ',
          'ทันทีที่เกิดแท่งสีแดงแท่งแรก',
          'เมื่อราคาพุ่งทะลุแนวต้านใหญ่ใน Timeframe Day'
        ],
        correctIndex: 1,
        explanation: 'หน้า 39 ระบุชัดเจนว่า "เราจะใช้ในการคอนเฟิร์ม HIGH, LOW และก็จะคอนเฟิร์มก็ต่อเมื่อ IDM ถูกเคลียร์ โครงสร้างของเทรนจะสร้างสวิง Valid Pullback หรือ IDM ขึ้นมาเสมอ"',
        referenceConcept: 'E-Book หน้า 39: Swing Confirmation via IDM'
      },
      {
        id: 'q7-2',
        type: 'mcq',
        question: 'หากสวิงที่เกิดขึ้น "ไม่ใช่ Valid Pullback ที่ถูกต้อง" สวิงนั้นสามารถนำมาใช้เป็น IDM ได้หรือไม่ตามหน้า 35 และ 38?',
        options: [
          'ได้ หากอยู่ใน Timeframe ใหญ่',
          'ได้ หากมีวอลุ่มการซื้อขายสูง',
          'ไม่ได้ หากไม่เกิดการสร้าง Valid Pullback ที่ถูกต้อง ก็จะยังไม่ใช่ IDM เช่นกัน',
          'ใช้ได้เฉพาะในเทรนขาลงเท่านั้น'
        ],
        correctIndex: 2,
        explanation: 'หน้า 35 และ 38 ระบุว่า "หากไม่เกิดการสร้าง Valid Pullback ที่ถูกต้อง ก็จะยังไม่ใช่ IDM เช่นกัน"',
        referenceConcept: 'E-Book หน้า 35, 38: เงื่อนไขการเกิด IDM'
      }
    ]
  },
  {
    id: 'ch-08-bos-idm-integration',
    chapterNumber: 8,
    title: 'BOS + IDM Integration (การรวมโครงสร้างสมบูรณ์)',
    englishTitle: 'Complete Market Cycle: BOS, IDM & Internal Structure',
    category: 'Structure',
    difficulty: 'Advanced',
    estimatedMinutes: 20,
    pdfPages: '53 - 55',
    shortDescription: 'การประกอบร่าง BOS และ IDM เข้าด้วยกัน โครงสร้างภายใน (Internal IDM) และการยืนยันเทรนแท้จริง',
    whyItMatters: 'การรวม BOS และ IDM คือสูตรลับของ Smart Money ที่คัดกรองสัญญาณหลอกออกไปได้มากกว่า 95%',
    summary: [
      'โครงสร้างหลักของ Market Structure ประกอบด้วย CHoCH และ BOS แต่ในการยืนยัน BOS ต้องมี IDM เข้ามาประกอบด้วย',
      'ลำดับที่สมบูรณ์: เคลียร์ IDM สำเร็จ -> คอนเฟิร์ม High/Low -> เบรค High/Low ด้วยเนื้อเทียน -> เกิด BOS ที่สมบูรณ์',
      'การหา IDM ภายใน (Internal IDM) จะหาได้เฉพาะในโครงสร้างของ BOS หรือ CHoCH เท่านั้น',
      'หากมีเพียงการสร้างสวิงเฉยๆ จะไม่สามารถหา IDM ภายในในสวิงนั้นได้'
    ],
    keyTerms: [
      { term: 'Complete SMC Cycle', meaning: 'วงจรสมบูรณ์: Sweep IDM -> Confirm Swing -> Body Break -> True BOS' },
      { term: 'Internal IDM', meaning: 'IDM ของโครงสร้างย่อยภายในกรอบสวิงหลัก ใช้เพื่อหาจุดเข้าในไทม์เฟรมเล็ก' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_053.png',
        caption: 'หน้า 53: BOS + IDM โครงสร้างตลาดที่สมบูรณ์ต้องมี IDM ประกอบ',
        page: 53
      },
      {
        url: '/extracted/page_renders/page_054.png',
        caption: 'หน้า 54: การหา IDM ภายใน (Internal IDM) เฉพาะในโครงสร้าง BOS หรือ CHoCH',
        page: 54
      },
      {
        url: '/extracted/page_renders/page_055.png',
        caption: 'หน้า 55: สวิงธรรมดาที่ไม่มี BOS ไม่สามารถหา IDM ภายในได้',
        page: 55
      }
    ],
    lessons: [
      {
        id: 'lesson-8-1',
        title: 'ลำดับวงจรโครงสร้างตลาด SMC ที่สมบูรณ์',
        content: `จากหน้า 53 ของ E-Book:
**"โครงสร้างหลักๆ ของ Market Structure ประกอบด้วย CHoCH, BOS แต่ในการยืนยัน BOS ต้องมี IDM เข้ามาประกอบด้วย"**

**ขั้นตอนวงจร SMC 4 สเต็ป (หน้า 53):**
1. **สเต็ป 1 (สร้างยอด):** ราคาวิ่งขึ้นไปทำยอด High แล้วเริ่มพักตัวทำ Valid Pullback ตัวแรก (กลายเป็น IDM)
2. **สเต็ป 2 (เคลียร์ IDM):** ราคาย่อตัวลงมากวาด/เคลียร์ IDM สำเร็จ ส่งผลให้ยอด High ก่อนหน้า **ได้รับการคอนเฟิร์ม (Confirmed High)**
3. **สเต็ป 3 (สะสมแรง):** ราคาลงมาทดสอบ Demand Zone / Order Block ด้านล่างแล้วดีดตัวขึ้น
4. **สเต็ป 4 (BOS แท้จริง):** ราคาพุ่งขึ้นไปและ **"ปิดเนื้อเทียนทะลุ Confirmed High"** ได้สำเร็จ จึงจะเกิด **BOS ที่สมบูรณ์แบบ!**

หากไม่มีการเคลียร์ IDM มาก่อน การทะลุ High ขึ้นไปจะไม่ใช่ BOS แต่เป็นเพียงการขยายคลื่นที่ไม่สมบูรณ์`,
        corePrinciples: [
          'BOS แท้จริงต้องเกิดขึ้นหลังจากเคลียร์ IDM แล้วเท่านั้น',
          'ถ้าไม่มีการเคลียร์ IDM ยอด High จะยังไม่คอนเฟิร์ม จึงไม่สามารถเกิด BOS ได้',
          'นี่คือเกราะป้องกันการโดนหลอกในตลาดการเงิน'
        ],
        practicalExamples: 'ในคู่ EUR/USD ราคาย่อกิน IDM ที่ 1.0800 ยืนยัน High 1.0850 จากนั้นราคาดีดตัวขึ้นไปปิดเนื้อเทียนที่ 1.0860 นั่นคือจุดเกิด BOS ของรอบอย่างแท้จริง',
        proTips: 'ท่องจำลำดับ: IDM Sweep -> Confirm High -> Candle Body Break -> Valid BOS',
        pitfalls: 'มองแค่การเบรคแนวนอนโดยไม่สนใจว่าราคาได้เคลียร์ IDM มาแล้วหรือยัง'
      }
    ],
    quiz: [
      {
        id: 'q8-1',
        type: 'mcq',
        question: 'ตามหน้า 53 ของ E-Book องค์ประกอบใดที่จำเป็นต้องมีเข้ามาประกอบ เพื่อยืนยันว่าเกิด BOS ที่แท้จริง?',
        options: [
          'ตัวชี้วัด RSI Overbought',
          'IDM (Inducement) ที่ถูกเคลียร์เพื่อคอนเฟิร์ม High ก่อนหน้า',
          'เส้นค่าเฉลี่ย EMA 200',
          'แท่งเทียน Doji 3 แท่ง'
        ],
        correctIndex: 1,
        explanation: 'หน้า 53 ระบุชัดเจนว่า "แต่ในการยืนยัน BOS ต้องมี IDM เข้ามาประกอบด้วย... BOS ที่เคลียร์ IDM ได้สำเร็จและเบรค High ได้"',
        referenceConcept: 'E-Book หน้า 53: BOS + IDM Integration'
      }
    ]
  },
  {
    id: 'ch-09-choch-mss',
    chapterNumber: 9,
    title: 'CHoCH & MSS (การเปลี่ยนทิศทางโครงสร้างตลาด)',
    englishTitle: 'Change of Character (CHoCH) & Market Structure Shift (MSS)',
    category: 'Structure',
    difficulty: 'Intermediate',
    estimatedMinutes: 25,
    pdfPages: '56 - 65',
    shortDescription: 'สัญญาณเตือนการกลับตัวของแนวโน้มใหญ่ กฎการเบรคด้วยเนื้อเทียน และความแตกต่างระหว่าง CHoCH กับ MSS',
    whyItMatters: 'CHoCH คือจุดกลับตัวที่ให้กำไรมหาศาล แต่ถ้าดูจุดผิด คุณจะเปิดออเดอร์สวนเทรนหลักที่กำลังพุ่งแรง',
    summary: [
      'CHoCH (Change of Character) คือ รูปแบบเมื่อราคาทำลายโครงสร้างของเทรน จาก Up Trend เป็น Down Trend หรือจาก Down Trend เป็น Up Trend',
      'กฎเหล็กของ CHoCH (หน้า 58): "CHoCH ที่ถูกต้อง ต้องถูกเบรคด้วยเนื้อเทียน"',
      'ใน Up Trend: จุดที่จะนับเป็น CHoCH คือจุด Low ต่ำสุดล่าสุดที่ส่งราคาขึ้นไปทำ Confirmed High',
      'MSS (Market Structure Shift) คือ การเปลี่ยนโครงสร้างแบบเฉียบพลันในกรอบเวลาย่อยหลังสัมผัส POI'
    ],
    keyTerms: [
      { term: 'CHoCH (Change of Character)', meaning: 'การเปลี่ยนสภาวะโครงสร้างจากขาขึ้นเป็นขาลง หรือขาลงเป็นขาขึ้น' },
      { term: 'MSS (Market Structure Shift)', meaning: 'การเปลี่ยนโครงสร้างเฉียบพลันใน Timeframe ย่อยเพื่อยืนยันการกลับตัว' },
      { term: 'Major Low (HL)', meaning: 'จุดต่ำสุดสำคัญที่ได้รับการคอนเฟิร์ม หากถูกเบรคด้วยเนื้อเทียนจะเกิด CHoCH' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_056.png',
        caption: 'หน้า 56: นิยาม CHoCH Change of Character (การทำลายโครงสร้างของเทรน)',
        page: 56
      },
      {
        url: '/extracted/page_renders/page_058.png',
        caption: 'หน้า 58: กฎเหล็ก CHoCH ที่ถูกต้อง ต้องถูกเบรคด้วยเนื้อเทียน',
        page: 58
      },
      {
        url: '/extracted/page_renders/page_063.png',
        caption: 'หน้า 63: MSS Market Structure Shift',
        page: 63
      }
    ],
    lessons: [
      {
        id: 'lesson-9-1',
        title: 'กลไกและกฎเหล็กของ CHoCH (Change of Character)',
        content: `จากหน้า 56-58 ของ E-Book:

**1. CHoCH คืออะไร?**
CHoCH คือการเปลี่ยนคาแรคเตอร์ของตลาด จากที่เคยทำ Higher High และ Higher Low ต่อเนื่อง จู่ๆ ราคากลับทิ้งตัวลงมาทำลายจุด Higher Low สำคัญ

**2. กฎการเบรคด้วยเนื้อเทียน (หน้า 58):**
**"CHoCH ที่ถูกต้อง ต้องถูกเบรคด้วยเนื้อเทียนเท่านั้น"**
หากราคาเพียงแค่ทิ้งไส้เทียนลงมาสะกิดหลุด Low แล้วดีดกลับขึ้นไปปิดเนื้อเหนือ Low **จะไม่นับเป็น CHoCH!** แต่จะนับเป็นการ "Liquidity Sweep" (กวาดสภาพคล่อง) ของฝั่ง Buy เพื่อพุ่งขึ้นต่อ!

**3. จุดอ้างอิง CHoCH ที่ถูกต้อง:**
ต้องเป็น Low ล่าสุดที่ส่งราคาขึ้นไปทำ High ที่ได้รับการเคลียร์ IDM แล้วเท่านั้น ห้ามใช้ Low ของสวิงย่อยภายในที่ไม่ผ่านเงื่อนไข`,
        corePrinciples: [
          'CHoCH ต้องปิดด้วยเนื้อเทียนแท่งเต็ม',
          'การหลุดด้วยไส้เทียน = Liquidity Sweep ห้ามเปิดออเดอร์กลับตัว',
          'จุดอ้างอิงต้องเป็น Major Low/High ของโครงสร้างหลัก'
        ],
        practicalExamples: 'ราคาอยู่ในขาขึ้น จุด Low สำคัญอยู่ที่ 1.2500 มีแท่งเทียนทิ้งตัวลงมาปิดเนื้อเทียนที่ 1.2480 นี่คือการยืนยัน CHoCH ทันที เทรนได้เปลี่ยนเป็นขาลงแล้ว ให้หยุดมองหาจุด Buy และเตรียมหาจุด Sell ที่โซน Supply ด้านบน',
        proTips: 'เมื่อเกิด CHoCH ครั้งแรก อย่าเพิ่งรีบ Sell ตามทันที ให้รอราคาย้อนกลับขึ้นมาเคลียร์ IDM และแตะ Supply Zone ก่อน',
        pitfalls: 'เห็นแท่งแดงยาวทะลุ Low ระหว่างแท่งแล้วกด Sell ทันที พอจบแท่งกลายเป็นไส้ยาวดีดกลับลากขาดทุน'
      }
    ],
    quiz: [
      {
        id: 'q9-1',
        type: 'mcq',
        question: 'ตามหน้า 58 ของ E-Book เงื่อนไขสำคัญที่สุดของ CHoCH ที่ถูกต้องคือข้อใด?',
        options: [
          'ต้องเกิดขึ้นในวันศุกร์เท่านั้น',
          'ต้องถูกเบรคด้วยเนื้อเทียน (Candle Body Break)',
          'ต้องใช้ไส้เทียนกวาดผ่านอย่างน้อย 3 ครั้ง',
          'ต้องเกิดร่วมกับข่าวเศรษฐกิจระดับสูง'
        ],
        correctIndex: 1,
        explanation: 'หน้า 58 ของ E-Book ระบุชัดเจนว่า "CHoCH ที่ถูกต้อง ต้องถูกเบรคด้วยเนื้อเทียน"',
        referenceConcept: 'E-Book หน้า 58: CHoCH Rules'
      }
    ]
  },
  {
    id: 'ch-10-liquidity-bsl-ssl',
    chapterNumber: 10,
    title: 'Liquidity (Lq), BSL & SSL (สภาพคล่องในตลาดการเงิน)',
    englishTitle: 'Liquidity Engineering: BSL, SSL, EQH & EQL',
    category: 'Liquidity',
    difficulty: 'Advanced',
    estimatedMinutes: 25,
    pdfPages: '66 - 72',
    shortDescription: 'ทำความเข้าใจ Liquidity เชื้อเพลิงของ Smart Money, Buy Side Liquidity (BSL) และ Sell Side Liquidity (SSL)',
    whyItMatters: 'ในตลาด Forex "ถ้าคุณมองไม่ออกว่า Liquidity อยู่ที่ไหน ตัวคุณนั่นแหละคือ Liquidity ให้คนอื่นกิน!"',
    summary: [
      'Liquidity (Lq) คือ บริเวณที่มีคำสั่ง Stop Loss และ Pending Orders ของรายย่อยกองอยู่หนาแน่น',
      'Smart Money ต้องการสภาพคล่องมหาศาลเพื่อจับคู่ออเดอร์ จึงต้องลากราคาไปกวาด Liquidity ก่อนเสมอ',
      'BSL (Buy Side Liquidity) คือ สภาพคล่องฝั่งซื้อ เหนือจุด Equal Highs (EQH) หรือยอด High ยอดนิยม',
      'SSL (Sell Side Liquidity) คือ สภาพคล่องฝั่งขาย ใต้จุด Equal Lows (EQL) หรือแนวรับยอดนิยม',
      'เมื่อเกิดการ Sweep Liquidity ราคาจะดึงตัวกลับอย่างรวดเร็ว'
    ],
    keyTerms: [
      { term: 'Liquidity (Lq)', meaning: 'สภาพคล่อง คำสั่งซื้อขายที่รออยู่ในตลาด เป็นเชื้อเพลิงผลักดันกราฟ' },
      { term: 'BSL (Buy Side Liquidity)', meaning: 'สภาพคล่องเหนือ Highs ที่มี Buy Stop และ SL ของฝั่ง Sell กองอยู่' },
      { term: 'SSL (Sell Side Liquidity)', meaning: 'สภาพคล่องใต้ Lows ที่มี Sell Stop และ SL ของฝั่ง Buy กองอยู่' },
      { term: 'EQH (Equal Highs)', meaning: 'ยอดราคาที่เท่ากันหรือใกล้เคียงกัน รายย่อยมองเป็นแนวต้าน แต่ SMC มองเป็นสภาพคล่อง' },
      { term: 'EQL (Equal Lows)', meaning: 'ก้นราคาที่เท่ากัน รายย่อยมองเป็นแนวรับ แต่ SMC มองเป็นจุดกวาดสภาพคล่อง' },
      { term: 'Liquidity Sweep', meaning: 'การที่ราคาทะลุระดับสำคัญด้วยไส้เทียนเพื่อกินคำสั่ง SL แล้วดีดกลับทันที' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_066.png',
        caption: 'หน้า 66: ตัวอย่างการเกิดการเคลียร์ LQ (Liquidity)',
        page: 66
      },
      {
        url: '/extracted/page_renders/page_069.png',
        caption: 'หน้า 69: นิยาม BSL (Buy Side Liquidity) และ SSL (Sell Side Liquidity)',
        page: 69
      },
      {
        url: '/extracted/page_renders/page_070.png',
        caption: 'หน้า 70: การ Sweep BSL เหนือ Equal Highs (EQH)',
        page: 70
      },
      {
        url: '/extracted/page_renders/page_071.png',
        caption: 'หน้า 71: การ Sweep SSL ใต้ Equal Lows (EQL)',
        page: 71
      }
    ],
    lessons: [
      {
        id: 'lesson-10-1',
        title: 'กลไก Liquidity: อาหารจานโปรดของ Smart Money',
        content: `จากหน้า 66-72 ของ E-Book:

**Liquidity คืออะไรในมุมมองสถาบัน?**
สถาบันการเงินต้องการเปิดออเดอร์ขนาดพันล้านดอลลาร์ พวกเขาไม่สามารถกด Buy ในราคาตลาดได้ทันทีเพราะจะทำให้ราคาพุ่งทะลุและได้ราคาแย่ (Slippage)
ทางเดียวที่สถาบันจะ Buy ได้จำนวนมหาศาล คือ **"ต้องหาคนที่มีคำสั่ง Sell ในปริมาณเท่ากันมารองรับ"**

แล้วคนจะยอม Sell ที่ไหนมากที่สุด?
1. คนที่ถือ Buy วาง **Stop Loss** ไว้ใต้แนวรับ (Stop Loss ของ Buy คือคำสั่ง Sell อัตโนมัติ!)
2. คนที่รอเปิดคำสั่ง **Sell Stop** เมื่อราคาหลุดแนวรับ

นี่คือเหตุผลที่กราฟมักจะทุบหลุดแนวรับ (EQL) ลงไปกวาดคำสั่งเหล่านั้น (Sell Side Liquidity - SSL) เพื่อให้สถาบันได้ของราคาถูก แล้วจากนั้นราคาก็ดีดตัวพุ่งขึ้นอย่างรุนแรง ทิ้งให้รายย่อยตกรถและขาดทุน!`,
        corePrinciples: [
          'ทุกแนวรับแนวต้านแบบดั้งเดิม (Double Top / Double Bottom) คือกับดักสภาพคล่อง',
          'BSL อยู่เหนือยอด High / EQH',
          'SSL อยู่ใต้ก้น Low / EQL',
          'รอให้เกิด Liquidity Sweep ก่อน แล้วจึงค่อยเข้าเทรด'
        ],
        practicalExamples: 'ราคาทำจุดต่ำสุดเท่ากัน 2 ครั้งที่ 1900 (Equal Lows) รายย่อยตั้ง Buy และวาง SL ที่ 1898 Smart Money ทุบราคาลงมาที่ 1895 แตะ SL ของทุกคน แล้วแท่งถัดไปดึงไส้กลับปิดเหนือ 1900 และพุ่งไป 1930 ทันที',
        proTips: 'อย่าเทรดที่ EQH/EQL แต่ให้ตั้งแจ้งเตือนไว้หลัง EQH/EQL เพื่อรอจังหวะที่ราคากวาดเสร็จแล้วกลับตัว',
        pitfalls: 'วาง Stop Loss ตรงแนวรับพอดีเป๊ะ ซึ่งเป็นเป้าหมายแรกที่ Smart Money จะวิ่งมากวาด'
      },
      {
        id: 'lesson-10-2',
        title: 'BSL vs SSL (หน้า 69-72)',
        content: `ในหน้า 69 ของ E-Book นิยามไว้อย่างชัดเจน:

- **SSL (Sell Side Liquidity):**
  "SSL คือ Low ที่ Sweep Liquidity โดยจะเป็นการรับ Liquidity ไปจาก EQL หรือ LQ"
  อยู่บริเวณใต้จุดต่ำสุดหรือแนวรับ

- **BSL (Buy Side Liquidity):**
  "BSL คือ High ที่ Sweep Liquidity จาก EQH หรือ LQ"
  อยู่บริเวณเหนือจุดสูงสุดหรือแนวต้าน

เมื่อสถาบันกวาด BSL สำเร็จ พวกเขาได้คู่สัญญาสำหรับเปิด Sell ในราคาแพงสุด จากนั้นตลาดจะกลับตัวลงอย่างรวดเร็ว`,
        corePrinciples: [
          'BSL = เป้าหมายทำกำไรของขา Buy / จุดดัก Sell ของสถาบัน',
          'SSL = เป้าหมายทำกำไรของขา Sell / จุดดัก Buy ของสถาบัน'
        ],
        practicalExamples: 'ในการวาง Take Profit ให้เล็งไปที่จุด BSL หรือ SSL ฝั่งตรงข้ามเสมอ เพราะเป็นจุดที่ราคามักถูกดึงดูดไปหาเหมือนแม่เหล็ก',
        proTips: 'ใช้ BSL/SSL เป็นเป้าหมาย TP เพื่อปิดกำไรก่อนที่ราคาจะเกิดการกลับตัว',
        pitfalls: 'พยายาม Sell ใต้ SSL เพราะคิดว่าราคาจะหลุดยาว ซึ่งมักเป็นจุดกลับตัวพอดี'
      }
    ],
    quiz: [
      {
        id: 'q10-1',
        type: 'mcq',
        question: 'ตามหน้า 69 ของ E-Book จุด BSL (Buy Side Liquidity) มักจะสะสมอยู่ที่บริเวณใด?',
        options: [
          'บริเวณใต้ Equal Lows (EQL)',
          'บริเวณ High ที่ Sweep Liquidity จาก Equal Highs (EQH) หรือ LQ ด้านบน',
          'ที่กึ่งกลางของคลื่นพักตัว',
          'ในบริเวณเส้น EMA 50'
        ],
        correctIndex: 1,
        explanation: 'หน้า 69 ระบุว่า "BSL คือ High ที่ Sweep Liquidity จาก EQH หรือ LQ" ซึ่งอยู่บริเวณเหนือจุดสูงสุดหรือแนวต้าน',
        referenceConcept: 'E-Book หน้า 69: BSL Definition'
      }
    ]
  },
  {
    id: 'ch-11-order-flow-of',
    chapterNumber: 11,
    title: 'Order Flow (OF) (การไหลของคำสั่งซื้อขายสถาบัน)',
    englishTitle: 'Order Flow (OF): Single-Use Zone Rule & Mitigations',
    category: 'Entry Execution',
    difficulty: 'Advanced',
    estimatedMinutes: 20,
    pdfPages: '73 - 77',
    shortDescription: 'ทำความเข้าใจ Order Flow กฎเหล็กการใช้งานเพียง 1 ครั้งเท่านั้น และความแตกต่างระหว่าง OF Major กับ Minor',
    whyItMatters: 'การเข้าซ้ำใน Order Flow ที่ถูก Mitigate ไปแล้ว เป็นสาเหตุอันดับหนึ่งของการขาดทุนของเทรดเดอร์มือใหม่',
    summary: [
      'Order Flow (OF) คือ แรงซื้อหรือแรงขายสุดท้าย ก่อนจะมีการปรับตัวขึ้นหรือลงต่อไป',
      'OF ในขาขึ้น คือ "แรงขายสุดท้ายก่อนมีการปรับตัวขึ้น" (Last selling move before rally)',
      'OF ในขาลง คือ "แรงซื้อสุดท้ายก่อนมีการปรับตัวลง" (Last buying move before drop)',
      'กฎเหล็กของ OF (หน้า 76): "สามารถใช้ได้เพียง 1 ครั้งเท่านั้น! จะไม่มีการเติมไม้ตอนที่ตลาดกลับมาทดสอบโซนซ้ำ"',
      'ทั้ง OF Major และ OF Minor ต้องผ่านเกณฑ์ Valid Pullback ที่ถูกต้อง'
    ],
    keyTerms: [
      { term: 'Order Flow (OF)', meaning: 'โซนคำสั่งซื้อขายสะสมของสถาบันก่อนเกิดการเคลื่อนที่ระเบิดออก' },
      { term: 'Single-Use Rule', meaning: 'กฎการใช้โซนได้เพียงครั้งเดียว เมื่อถูกทดสอบแล้วจะไม่นำกลับมาใช้อีก' },
      { term: 'Mitigation', meaning: 'การที่ราคากลับมาแตะเพื่อปิดคำสั่งค้างหรือปลดล็อกออเดอร์ของสถาบัน' },
      { term: 'Unmitigated Zone', meaning: 'โซนบริสุทธิ์ที่ยังไม่เคยถูกราคาย้อนกลับมาแตะเลย มีโอกาสชนะสูงที่สุด' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_073.png',
        caption: 'หน้า 73: นิยาม Order Flow (OF) แรงซื้อ/แรงขายสุดท้าย',
        page: 73
      },
      {
        url: '/extracted/page_renders/page_075.png',
        caption: 'หน้า 75: แรงลงสุดท้ายก่อนปรับตัวขึ้น จัดอยู่ในหมวดหมู่ Valid Pullback ที่ถูกต้อง',
        page: 75
      },
      {
        url: '/extracted/page_renders/page_076.png',
        caption: 'หน้า 76: กฎเหล็ก OF ใช้ได้เพียง 1 ครั้งเท่านั้น ไม่มีการเติมไม้ซ้ำ',
        page: 76
      },
      {
        url: '/extracted/page_renders/page_077.png',
        caption: 'หน้า 77: Order Flow Major และ Minor ทั้งสองต้องทำ Valid Pullback ที่ถูกต้อง',
        page: 77
      }
    ],
    lessons: [
      {
        id: 'lesson-11-1',
        title: 'นิยามและกฎเหล็กการใช้งาน Order Flow (OF)',
        content: `จากหน้า 73-77 ของ E-Book:

**1. Order Flow คืออะไร? (หน้า 73)**
- **Bullish OF:** คือ "แรงขายสุดท้ายก่อนที่จะมีการปรับตัวขึ้น"
- **Bearish OF:** คือ "แรงซื้อสุดท้ายก่อนที่จะมีการปรับตัวลง"
- และแรงลงหรือขึ้นสุดท้ายนั้น **ต้องจัดอยู่ในหมวดหมู่ของการทำ Valid Pullback ที่ถูกต้อง (หน้า 75)**

**2. กฎเหล็กของการใช้ Order Flow (หน้า 76):**
**"เงื่อนไขของ OF คือสามารถใช้ได้เพียง 1 ครั้งเท่านั้น! จะไม่มีการเติมไม้ตอนที่ตลาดกลับมาทดสอบโซน และต้องทำ Valid Pullback ที่ถูกต้อง"**

**ทำไมถึงใช้ได้แค่ครั้งเดียว?**
เพราะเมื่อราคาย้อนกลับมาแตะ OF ในครั้งแรก สถาบันการเงินได้ทำการ "Mitigate" (ปิดออเดอร์ที่เคยขาดทุนและเติมคำสั่งชุดใหม่จนหมดแล้ว) หากราคาวนกลับมาอีกรอบ โซนนั้นจะไม่มีออเดอร์ค้างอยู่อีกต่อไป ราคามักจะทะลุผ่านไปอย่างไร้ความปรานี!`,
        corePrinciples: [
          'Order Flow ใช้ได้เพียง 1 ครั้งเท่านั้น',
          'โซนที่ถูกแตะไปแล้ว (Mitigated) ห้ามเข้าเทรดซ้ำเด็ดขาด',
          'OF ต้องเกิดจาก Valid Pullback ที่ถูกต้อง'
        ],
        practicalExamples: 'ราคาดีดขึ้นจาก OF รอบแรก 50 จุด เมื่อราคาย้อนกลับมาทดสอบที่จุดเดิมเป็นครั้งที่สอง เทรดเดอร์ SMC จะไม่เปิด Buy ซ้ำ แต่จะมองว่าโซนนี้หมดสภาพและเตรียมรอจังหวะทะลุ',
        proTips: 'เลือกเทรดเฉพาะ Unmitigated OF เท่านั้น เพื่อรักษา Win Rate ในระดับสูงสุด',
        pitfalls: 'เทรดแบบแนวรับแนวต้านดั้งเดิมที่ยิ่งทดสอบหลายครั้งยิ่งคิดว่าแข็งแกร่ง ใน SMC ยิ่งทดสอบหลายครั้งยิ่งอ่อนแอและพร้อมแตก'
      }
    ],
    quiz: [
      {
        id: 'q11-1',
        type: 'mcq',
        question: 'ตามหน้า 76 ของ E-Book กฎเหล็กที่สำคัญที่สุดของ Order Flow (OF) คือข้อใด?',
        options: [
          'สามารถใช้เติมไม้ได้เรื่อยๆ ตราบใดที่ราคายังไม่หลุด',
          'สามารถใช้ได้เพียง 1 ครั้งเท่านั้น จะไม่มีการเติมไม้ตอนที่ตลาดกลับมาทดสอบโซนซ้ำ',
          'ใช้ได้เฉพาะในกรอบเวลา 1 นาทีเท่านั้น',
          'ต้องรอให้เกิดข่าวใหญ่ก่อนจึงจะใช้ได้'
        ],
        correctIndex: 1,
        explanation: 'หน้า 76 ระบุอย่างชัดเจนว่า "เงื่อนไขของ OF คือสามารถใช้ได้เพียง 1 ครั้งเท่านั้นจะไม่มีการเติมไม้ตอนที่ตลาดกลับมาทดสอบโซนและต้องทำ Valid Pullback ที่ถูกต้อง"',
        referenceConcept: 'E-Book หน้า 76: กฎเหล็กของ OF'
      }
    ]
  },
  {
    id: 'ch-12-order-blocks-scob',
    chapterNumber: 12,
    title: 'Order Blocks (OB) & Single Candle Order Block (SCOB)',
    englishTitle: 'Advanced Order Blocks (OB) & SCOB Execution',
    category: 'Entry Execution',
    difficulty: 'Advanced',
    estimatedMinutes: 30,
    pdfPages: '78 - 90',
    shortDescription: 'สุดยอดจุดเข้าเทรดของสถาบัน: การหา OB แท้จริงที่มี FVG + Liquidity Sweep และเทคนิค SCOB ยืนยันแท่งเดียว',
    whyItMatters: 'Order Block แท้จริงให้จุดเข้าที่คมกริบ Stop Loss สั้นมาก และมี Risk:Reward ตั้งแต่ 1:5 ไปจนถึง 1:20+',
    summary: [
      'Order Block (OB) คือ แท่งเทียนตรงข้ามแท่งสุดท้ายก่อนเกิด Impulse Move ที่รุนแรง',
      'คุณสมบัติของ OB ที่มีประสิทธิภาพสูงสุด: ต้องมีการ Sweep Liquidity ก่อนหน้า + ต้องมี Imbalance (FVG) ชัดเจน + ต้องยังไม่ถูกทดสอบ (Unmitigated)',
      'SCOB (Single Candle Order Block) คือ การใช้แท่งเทียนแท่งเดียวในการยืนยันจุดเข้าเทรดหลังจากราคามาแตะ POI',
      'เงื่อนไข SCOB: แท่งที่ 1 กวาด (Sweep) High หรือ Low ของแท่งก่อนหน้า แล้วแท่งที่ 2 ปิดเนื้อคลุมไส้'
    ],
    keyTerms: [
      { term: 'Order Block (OB)', meaning: 'แท่งเทียนต้นกำเนิดคำสั่งสถาบันที่ทำให้เกิดการเบรคโครงสร้างและสร้าง FVG' },
      { term: 'SCOB (Single Candle OB)', meaning: 'แท่งเทียนแท่งเดี่ยวที่ยืนยันการกลับตัวในระดับแท่งเทียนหลังแตะ POI' },
      { term: 'Unmitigated OB', meaning: 'Order Block ที่ยังไม่เคยมีไส้หรือเนื้อเทียนใดๆ กลับมาสัมผัสเลย' },
      { term: 'Sweep and Close', meaning: 'การกวาดสภาพคล่องของแท่งก่อนหน้าแล้วปิดเนื้อเทียนยืนยันในทิศทางตรงข้าม' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_078.png',
        caption: 'หน้า 78: นิยาม Order Block (OB)',
        page: 78
      },
      {
        url: '/extracted/page_renders/page_081.png',
        caption: 'หน้า 81: ลักษณะของ OB ที่มีคุณภาพสูง',
        page: 81
      },
      {
        url: '/extracted/page_renders/page_085.png',
        caption: 'หน้า 85: Single Candle Order Block (SCOB)',
        page: 85
      },
      {
        url: '/extracted/page_renders/page_086.png',
        caption: 'หน้า 86: เงื่อนไขการใช้ SCOB หลังราคาแตะ POI หรือโซนสำคัญ',
        page: 86
      },
      {
        url: '/extracted/page_renders/page_088.png',
        caption: 'หน้า 88: การ Sweep Low แท่งก่อนหน้าของรูปแบบ SCOB',
        page: 88
      },
      {
        url: '/extracted/page_renders/page_089.png',
        caption: 'หน้า 89: กรณีแท่งที่ 1 Sweep แล้วแต่แท่งที่ 2 ไม่สามารถปิดเนื้อคลุมไส้ได้',
        page: 89
      }
    ],
    lessons: [
      {
        id: 'lesson-12-1',
        title: 'การคัดกรอง Order Block (OB) คุณภาพสูง',
        content: `จากหน้า 78-84 ของ E-Book:

**Order Block คืออะไร?**
OB คือแท่งเทียนแท่งสุดท้ายที่สถาบันใช้เปิดคำสั่งสวนทางเพื่อล่อสภาพคล่อง ก่อนที่จะอัดเม็ดเงินมหาศาลผลักดันราคาไปในทิศทางจริง

**3 คุณสมบัติคัดกรอง OB คุณภาพสูง:**
1. **ต้องมีการ Sweep Liquidity:** แท่ง OB นั้นจะต้องเคยกวาด High หรือ Low ของแท่งก่อนหน้า เพื่อกวาด Stop Loss ของรายย่อยมาแล้ว
2. **ต้องมี FVG (Fair Value Gap / Imbalance):** แท่งเทียนที่พุ่งออกจาก OB จะต้องมีความไม่สมดุลของราคาอย่างชัดเจน ทิ้งช่องว่าง FVG ไว้
3. **ต้องส่งผลให้เกิด BOS หรือ CHoCH:** แรงส่งจาก OB ต้องมากพอที่จะทำลายโครงสร้างตลาด
4. **ต้องเป็น Unmitigated:** ราคาไม่เคยย้อนกลับมาสัมผัสเลยนับตั้งแต่ถูกสร้างขึ้น`,
        corePrinciples: [
          'ไม่ใช่แท่งสีตรงข้ามทุกแท่งจะเป็น OB',
          'OB ต้องมี FVG อยู่ติดกับตัวแท่งเสมอ',
          'OB ที่ผ่านการ Sweep สภาพคล่องมาแล้ว คือ OB เกรด A+'
        ],
        practicalExamples: 'ก่อนที่ราคาทองจะพุ่งทะลุ 2300 มีแท่งแดงแท่งหนึ่งที่ทุบกวาด Low ก่อนหน้า แล้วตามด้วยแท่งเขียวยักษ์ทิ้งช่องว่าง FVG แท่งแดงนั้นคือ Bullish Order Block คุณภาพสูง ให้วาง Buy Limit ไว้ที่ขอบบนของแท่งแดงนั้น',
        proTips: 'วัดอัตราส่วน R:R จากขอบ OB ไปยังเป้าหมาย หากได้ต่ำกว่า 1:3 ให้ข้ามไปหาโซนอื่น',
        pitfalls: 'ตีกรอบ OB ทุกแท่งที่เห็นในกราฟจนรกหน้าจอ ต้องเลือกเฉพาะแท่งที่มีคุณสมบัติครบ 3 ประการเท่านั้น'
      },
      {
        id: 'lesson-12-2',
        title: 'SCOB (Single Candle Order Block) ยืนยันจุดเข้าคมกริบ',
        content: `ในหน้า 85-90 ของ E-Book นำเสนอเทคนิคขั้นสูง:

**SCOB คืออะไร? (หน้า 85-86)**
"SCOB จะใช้ได้ก็ต่อเมื่อ **เกิดหลังจากมีการแตะ POI หรือโซนต่างๆ เท่านั้น** ใช้ในการ Confirm จุดเข้าเทรด"

**เงื่อนไขการเกิด SCOB (หน้า 86-89):**
1. ราคาวิ่งเข้ามาสัมผัสกรอบ POI (เช่น แตะ Demand Zone หรือ Bearish OB)
2. **แท่งที่ 1:** ทำการ **Sweep High หรือ Sweep Low** ของแท่งก่อนหน้า เพื่อดูดซับสภาพคล่องสุดท้าย
3. **แท่งที่ 2:** จะต้องสามารถ **"ปิดเนื้อเทียนคลุมไส้" (Body Close covers Wick)** ของแท่งที่ 1 ได้อย่างชัดเจน
4. **กรณีพิเศษ (หน้า 89):** หากแท่งที่ 1 Sweep แล้ว แต่แท่งที่ 2 ไม่สามารถปิดเนื้อคลุมไส้ได้ เราจะต้องรอแท่งถัดไปจนกว่าจะมีการปิดเนื้อคลุมไส้ จึงจะสมบูรณ์`,
        corePrinciples: [
          'SCOB ใช้ได้เฉพาะเมื่อราคาแตะ POI แล้วเท่านั้น',
          'แท่งแรกต้อง Sweep High/Low',
          'แท่งสองต้องปิดเนื้อคลุมไส้ของแท่งแรก',
          'จุดเข้าคือการตั้ง Limit ที่ไส้หรือเนื้อของแท่ง SCOB'
        ],
        practicalExamples: 'ราคาวิ่งมาชน Supply Zone H1 ใน M5 เกิดแท่งที่ 1 แทงไส้ทะลุ High ขึ้นไปแล้วดึงกลับ แท่งที่ 2 ทิ้งตัวลงมาปิดเนื้อต่ำกว่า Low ของแท่งที่ 1 ทันที เกิดเป็น Bearish SCOB เราเปิด Sell โดยวาง SL เหนือปลายไส้แท่งที่ 1 เพียงไม่กี่จุด!',
        proTips: 'SCOB ช่วยลดระยะ Stop Loss จากเดิม 20-30 จุด เหลือเพียง 5-8 จุด ทำให้ขยาย Lot Size ได้อย่างปลอดภัยตามระบบ MM',
        pitfalls: 'ใช้ SCOB กลางอากาศโดยที่ราคายังไม่แตะ POI สำคัญ ทำให้เกิดสัญญาณหลอกบ่อยครั้ง'
      }
    ],
    quiz: [
      {
        id: 'q12-1',
        type: 'mcq',
        question: 'ตามหน้า 86 ของ E-Book การนำ Single Candle Order Block (SCOB) มาใช้ จะทำได้ในสภาวะใดเท่านั้น?',
        options: [
          'ใช้ตอนไหนก็ได้ในตลาดเปิด',
          'ใช้ได้ก็ต่อเมื่อเกิดหลังจากราคาแตะ POI หรือโซนต่างๆ เท่านั้น เพื่อใช้ในการ Confirm',
          'ใช้เฉพาะตอนที่มีข่าวเศรษฐกิจ',
          'ใช้ได้เฉพาะในวันจันทร์ช่วงตลาดเปิด'
        ],
        correctIndex: 1,
        explanation: 'หน้า 86 ระบุชัดเจนว่า "โดย SCOB จะใช้ได้ก็ต่อเมื่อเกิดหลังจากมีการแตะ POI หรือโซนต่างๆ เท่านั้นใช้ในการ Confirm"',
        referenceConcept: 'E-Book หน้า 86: เงื่อนไขการใช้ SCOB'
      },
      {
        id: 'q12-2',
        type: 'scenario',
        question: 'ตามหน้า 88-89 หากแท่งที่ 1 ได้ทำการ Sweep Low ของแท่งก่อนหน้าแล้ว แต่แท่งที่ 2 ไม่สามารถปิดเนื้อเทียนคลุมไส้ของแท่งที่ 1 ได้ เราควรทำอย่างไร?',
        options: [
          'รีบกดเปิดออเดอร์ทันทีไม่ต้องรอ',
          'ยกเลิกแผนเทรดและปิดหน้าจอ',
          'รอแท่งถัดไปจนกว่าจะเกิดแท่งที่ปิดเนื้อเทียนคลุมไส้ได้อย่างสมบูรณ์',
          'เปลี่ยนไปเปิด Sell สวนทางทันที'
        ],
        correctIndex: 2,
        explanation: 'หน้า 89 ระบุว่า ในกรณีที่แท่งที่ 1 ได้ Sweep Low แล้วแต่แท่งที่ 2 ยังไม่สามารถปิดเนื้อคลุมไส้ได้ โครงสร้างยังไม่สมบูรณ์ เราต้องรอการยืนยันจนกว่าจะมีแท่งที่ปิดเนื้อคลุมได้',
        referenceConcept: 'E-Book หน้า 89: เงื่อนไขการปิดเนื้อคลุมไส้ของ SCOB'
      }
    ]
  },
  {
    id: 'ch-13-breaker-block-bb-brk',
    chapterNumber: 13,
    title: 'Breaker Block (BB & BRK) (บล็อกพลิกกลับ)',
    englishTitle: 'Break Block (BB) vs Breaker Block (BRK) Flip Zones',
    category: 'Entry Execution',
    difficulty: 'Advanced',
    estimatedMinutes: 20,
    pdfPages: '91 - 95',
    shortDescription: 'เมื่อโซนรับกลายเป็นโซนต้าน: ความแตกต่างระหว่าง Break Block (เบรคไปกลับ 2 รอบ) กับ Breaker Block (เบรคครั้งเดียว)',
    whyItMatters: 'เมื่อ Order Block ล้มเหลว อย่าเพิ่งตกใจ เพราะมันจะกลายร่างเป็น Breaker Block ที่ทรงพลังอย่างยิ่ง',
    summary: [
      'BB (Break Block) คือ Demand & Supply ใน Timeframe เล็ก ที่ถูกเบรคไป-กลับ 2 รอบ และนำกลับมาใช้ใหม่ (หน้า 91)',
      'การหา BB ที่มีประสิทธิภาพสูงสุด คือการหา BB ที่อยู่ใน Order Block (หน้า 91)',
      'BRK (Breaker Block) คือ Order Block (Demand & Supply) ที่ถูกเบรคเพียงครั้งเดียว แล้วนำกลับมาใช้ (หน้า 94)',
      'BRK จะสลับหน้าที่: จาก OB Demand เปลี่ยนเป็น OB Supply หรือจาก OB Supply เปลี่ยนเป็น OB Demand'
    ],
    keyTerms: [
      { term: 'BB (Break Block)', meaning: 'โซนในไทม์เฟรมเล็กที่ถูกเบรคทะลุไปกลับ 2 รอบ' },
      { term: 'BRK (Breaker Block)', meaning: 'Order Block ที่ล้มเหลว ถูกเบรคครั้งเดียวแล้วสลับขั้วเป็น Flip Zone' },
      { term: 'Flip Zone', meaning: 'การสลับหน้าที่จากแนวรับเป็นแนวต้าน หรือแนวต้านเป็นแนวรับ' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_091.png',
        caption: 'หน้า 91: นิยาม BB Break Block (เบรคไปกลับ 2 รอบ และหาใน OB)',
        page: 91
      },
      {
        url: '/extracted/page_renders/page_094.png',
        caption: 'หน้า 94: นิยาม BRK Breaker Block (OB ที่ถูกเบรคครั้งเดียวแล้วนำกลับมาใช้)',
        page: 94
      },
      {
        url: '/extracted/page_renders/page_095.png',
        caption: 'หน้า 95: BRK ในรูปแบบการทำ Pullback ที่ถูกต้อง',
        page: 95
      }
    ],
    lessons: [
      {
        id: 'lesson-13-1',
        title: 'ความแตกต่างเชิงโครงสร้างระหว่าง BB และ BRK',
        content: `จากหน้า 91-95 ของ E-Book:

**1. Break Block (BB) (หน้า 91):**
- BB คือ Demand หรือ Supply ใน Low Timeframe ที่เล็กที่สุด
- **ถูกราคาพุ่งเบรคทะลุไป-กลับถึง "2 รอบ"**
- จากนั้นราคาย้อนกลับมาทดสอบ และนำกลับมาใช้ใหม่
- **เคล็ดลับระดับเซียน (หน้า 91):** "การหา BB ที่มีประสิทธิภาพมากที่สุด คือการหา BB ที่แฝงตัวซ้อนทับอยู่ใน Order Block"

**2. Breaker Block (BRK) (หน้า 94):**
- BRK คือ Order Block Demand หรือ Supply **"ที่ถูกเบรคครั้งเดียว"** ด้วยโมเมนตัมรุนแรง
- นำกลับมาใช้โดยการสลับคุณสมบัติ:
  - จาก **OB Demand** กลายเป็น **OB Supply** (รับกลายเป็นต้าน)
  - จาก **OB Supply** กลายเป็น **OB Demand** (ต้านกลายเป็นรับ)
- ทั้งคู่จะต้องเกิดขึ้นร่วมกับการทำ Valid Pullback ที่ถูกต้อง (หน้า 93, 95)`,
        corePrinciples: [
          'BB = ถูกเบรคไปกลับ 2 รอบ (Double Break)',
          'BRK = ถูกเบรคครั้งเดียว (Single Break Flip)',
          'เมื่อราคาเบรค OB ทะลุรุนแรง อย่าเพิ่งเสียดาย ให้เตรียมกางไม้รอที่จุด BRK'
        ],
        practicalExamples: 'โซน Demand 1.1000 รับราคาไม่อยู่ โดนแท่งแดงยาวพุ่งทะลุลงไป 1.0950 โซน 1.1000 นั้นจะเปลี่ยนสภาพเป็น BRK Supply ทันที เมื่อราคาย้อนกลับมาทดสอบ 1.1000 ให้เปิด Sell ทันที!',
        proTips: 'BRK ที่เกิดขึ้นหลังการ Sweep Liquidity ฝั่งตรงข้าม จะมีความแม่นยำสูงมาก เพราะเป็นการยืนยันว่าสถาบันทิ้งออเดอร์เดิมและกลับทิศทางแล้ว',
        pitfalls: 'พยายามดันทุรัง Buy ในโซน Demand เดิมที่ถูกเบรคทะลุไปแล้ว แทนที่จะเปลี่ยนมุมมองมา Sell ที่ BRK'
      }
    ],
    quiz: [
      {
        id: 'q13-1',
        type: 'mcq',
        question: 'ตามหน้า 94 ของ E-Book Breaker Block (BRK) มีนิยามและการทำงานอย่างไร?',
        options: [
          'คือเส้นค่าเฉลี่ยที่ตัดกัน 2 ครั้ง',
          'คือ OB Demand & Supply ที่ถูกเบรคครั้งเดียว แล้วนำกลับมาใช้โดยจะเปลี่ยนคุณสมบัติขั้วตรงข้าม',
          'คือโซนที่ไม่เคยถูกราคาแตะเลยตลอดทั้งปี',
          'คือรูปแบบกราฟแท่งเทียน Doji 4 แท่ง'
        ],
        correctIndex: 1,
        explanation: 'หน้า 94 ระบุว่า "BRK คือ OB Demand&Supply ที่ถูกเบรคครั้งเดียว แล้วนำกลับมาใช้โดยจะเปลี่ยนคุณสมบัติจาก OB Demand เป็น OB Supply จาก OB Supply เปลี่ยนเป็น OB Demand"',
        referenceConcept: 'E-Book หน้า 94: Breaker Block (BRK)'
      }
    ]
  },
  {
    id: 'ch-14-poi-fvg',
    chapterNumber: 14,
    title: 'POI (Point of Interest) & FVG (Fair Value Gap)',
    englishTitle: 'Point of Interest Confluence & Fair Value Gaps',
    category: 'Entry Execution',
    difficulty: 'Advanced',
    estimatedMinutes: 25,
    pdfPages: '96 - 105',
    shortDescription: 'การเลือกจุดเข้าเทรดที่มีนัยสำคัญสูงสุด (POI) และการค้นหาช่องว่างราคาที่ไม่สมดุล (FVG / Imbalance)',
    whyItMatters: 'POI ช่วยกรองกราฟให้เหลือเพียง 1-2 จุดที่คุ้มค่าที่สุดในการรอคอย ไม่ต้องนั่งเฝ้าจอทั้งวัน',
    summary: [
      'POI (Point of Interest) คือ จุดที่มีความน่าสนใจหรือโซนที่มีนัยสำคัญในการเข้าออเดอร์ (หน้า 96)',
      'POI ที่ดีที่สุด คือจุดที่มีการ "ทับซ้อนกันของหลายๆ โซน" (Confluence) เช่น HTF OB + FVG + Liquidity Sweep',
      'FVG (Fair Value Gap / Imbalance) คือ การซื้อขายที่ไม่สมดุลทำให้เกิดช่องว่างระหว่างราคา (หน้า 103)',
      'FVG วัดจากช่องว่างระหว่างไส้เทียนของแท่งที่ 1 และไส้เทียนของแท่งที่ 3 โดยมีแท่งที่ 2 คั่นกลาง'
    ],
    keyTerms: [
      { term: 'POI (Point of Interest)', meaning: 'โซนเป้าหมายหลักที่มีนัยสำคัญสูงสุดสำหรับการรอเข้าออเดอร์' },
      { term: 'FVG (Fair Value Gap)', meaning: 'ช่องว่างความไม่สมดุลของราคา 3 แท่งเทียนที่ตลาดต้องกลับมาเติมเต็ม' },
      { term: 'Imbalance', meaning: 'ภาวะความไม่สมดุลของออเดอร์ซื้อขายที่มีฝั่งใดฝั่งหนึ่งล้นตลาด' },
      { term: 'Confluence', meaning: 'การรวมกันของหลายเงื่อนไขทางเทคนิคในจุดเดียวกันเพื่อเพิ่มความน่าจะเป็น' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_096.png',
        caption: 'หน้า 96: นิยาม POI Point of Interest Database ใน Timeframe H1',
        page: 96
      },
      {
        url: '/extracted/page_renders/page_103.png',
        caption: 'หน้า 103: นิยาม FVG (Fair Value Gap) การซื้อขายที่ไม่สมดุล',
        page: 103
      },
      {
        url: '/extracted/page_renders/page_104.png',
        caption: 'หน้า 104: ลักษณะของกราฟที่ไม่เปิด FVG (ราคา Balance สมดุล)',
        page: 104
      },
      {
        url: '/extracted/page_renders/page_105.png',
        caption: 'หน้า 105: กราฟที่มี FVG ชัดเจนและราคาย้อนกลับมาทดสอบ',
        page: 105
      }
    ],
    lessons: [
      {
        id: 'lesson-14-1',
        title: 'การประกอบร่าง POI (Point of Interest) คุณภาพสูงสุด',
        content: `จากหน้า 96-102 ของ E-Book:

**POI คืออะไร? (หน้า 96)**
"POI คือ จุดที่มีความน่าสนใจหรือโซนที่มีนัยสำคัญในการเข้าออเดอร์ ซึ่งเป็นจุดที่มีการ **ทับซ้อนโซนต่างๆ ไว้มากในบริเวณนั้น**"

**สูตร Confluence ของ POI ระดับพรีเมียม:**
1. อยู่ในกรอบเวลาใหญ่ (Higher Timeframe เช่น H4 หรือ H1)
2. เป็น Unmitigated Order Block ที่ยังสดใหม่
3. มีช่องว่าง FVG รองรับอยู่หน้าโซน
4. ตั้งอยู่ใน **Discount Zone** (สำหรับมองหา Buy) หรือ **Premium Zone** (สำหรับมองหา Sell)
5. มีสภาพคล่อง (Liquidity/IDM) ขวางอยู่ก่อนถึงโซน เพื่อเป็นเหยื่อล่อราคาให้วิ่งเข้ามาชน`,
        corePrinciples: [
          'อย่าเข้าเทรดสุ่มสี่สุ่มห้า ให้รอราคาเดินทางมาถึง POI เท่านั้น',
          'POI ยิ่งมีการทับซ้อนหลายปัจจัย ยิ่งมีอัตราการชนะสูง',
          'เมื่อราคามาถึง POI ให้สลับไป Low Timeframe เพื่อรอสัญญาณคอนเฟิร์ม (เช่น CHoCH / SCOB)'
        ],
        practicalExamples: 'เรากำหนด POI ที่ Demand Zone H1 ที่ราคา 2310 ซึ่งตรงกับ Fibonacci 0.705 และมี FVG ชัดเจน เราจะไม่กด Buy ทันที แต่จะรอให้ราคาลงมาแตะ 2310 แล้วเปิดดู M5 เพื่อรอแท่ง SCOB คอนเฟิร์ม',
        proTips: 'บันทึก POI ไว้ในกราฟล่วงหน้าช่วงตลาดเปิด แล้วตั้ง Alert เตือน ไม่ต้องเฝ้าจอตลอดเวลา',
        pitfalls: 'เทรดทุกสวิงที่เกิดขึ้นในไทม์เฟรม 1 นาทีโดยไม่มี POI ของไทม์เฟรมใหญ่คอยคุมทิศทาง'
      },
      {
        id: 'lesson-14-2',
        title: 'FVG (Fair Value Gap) ช่องว่างความไม่สมดุลของราคา',
        content: `จากหน้า 103-105 ของ E-Book:

**FVG คืออะไร? (หน้า 103)**
"FVG คือการซื้อขายที่ไม่สมดุล ทำให้เกิดช่องว่างระหว่างการซื้อหรือขาย (หรือที่เรียกว่า Imbalance)"

**วิธีการวัด FVG 3 แท่งเทียน:**
- พิจารณาแท่งเทียน 3 แท่งเรียงกัน: แท่งที่ 1, แท่งที่ 2 (แท่งยาว Impulse), และแท่งที่ 3
- **Bullish FVG:** วัดช่องว่างระหว่าง **"ปลายไส้บนของแท่งที่ 1"** กับ **"ปลายไส้ล่างของแท่งที่ 3"** หากไส้ทั้งสองไม่ซ้อนทับกัน จะเกิดช่องว่างขึ้น นั่นคือ FVG!
- **กราฟที่ไม่มี FVG (หน้า 104):** คือกราฟที่ไส้ของแท่ง 1 และแท่ง 3 เหลื่อมล้ำทับกัน แปลว่าตลาดมีการจับคู่ออเดอร์สมบูรณ์ (Efficient Market)`,
        corePrinciples: [
          'FVG คือแม่เหล็กดึงดูดราคา ตลาดจะวิ่งกลับมาปิดช่องว่างนี้เสมอ',
          'FVG สามารถใช้เป็นจุดเข้าเทรดเดี่ยวๆ หรือใช้ร่วมกับ OB ก็ได้',
          'เมื่อ FVG ถูกเติมเต็มจนครบ (Filled) ราคาจะกลับตัวไปตามเทรนเดิม'
        ],
        practicalExamples: 'แท่งที่ 1 มี High 100 แท่งที่ 2 พุ่งแรงจาก 99 ไป 120 แท่งที่ 3 มี Low ลงมาแค่ 105 ช่องว่างระหว่าง 100 ถึง 105 (ขนาด 5 จุด) คือ FVG เมื่อราคาถอยลงมาแตะ 103 ในช่องว่างนี้ ให้มองหาจังหวะ Buy ทันที',
        proTips: 'เลือกลงทุนใน FVG ที่เกิดขึ้นพร้อมกับการเบรค BOS เท่านั้น เพราะมีแรงสถาบันหนุนหลัง',
        pitfalls: 'คิดว่าราคาทุกช่องว่างต้องถูกปิดในทันที บางครั้งราคาอาจเดินทางต่อไปไกลก่อนจะวนกลับมาปิดในอนาคต'
      }
    ],
    quiz: [
      {
        id: 'q14-1',
        type: 'mcq',
        question: 'ตามหน้า 103 ของ E-Book FVG (Fair Value Gap) เกิดจากสาเหตุใด?',
        options: [
          'การที่ตลาดปิดทำการในวันหยุดสุดสัปดาห์',
          'การซื้อขายที่ไม่สมดุลทำให้เกิดช่องว่างระหว่างการซื้อหรือขาย (Imbalance)',
          'การตั้งค่าอินดิเคเตอร์ผิดพลาดของโบรกเกอร์',
          'การเทรดของเทรดเดอร์รายย่อยพร้อมกัน'
        ],
        correctIndex: 1,
        explanation: 'หน้า 103 ระบุว่า "FVG คือ การซื้อขายที่ไม่สมดุลทำให้เกิดช่องว่างระหว่างการซื้อหรือขาย (หรือที่เรียกว่า Imbalance)"',
        referenceConcept: 'E-Book หน้า 103: Fair Value Gap Definition'
      }
    ]
  },
  {
    id: 'ch-15-fibonacci-premium-discount',
    chapterNumber: 15,
    title: 'Fibonacci Retracement & โซนของถูกของแพง (Premium/Discount)',
    englishTitle: 'Fibonacci Retracement: Premium vs Discount Zones',
    category: 'Entry Execution',
    difficulty: 'Intermediate',
    estimatedMinutes: 20,
    pdfPages: '106 - 111',
    shortDescription: 'การใช้ Fibonacci แบ่งโซน 50% ของถูก (Discount) และของแพง (Premium) เพื่อไม่ให้ซื้อแพงหรือขายถูก',
    whyItMatters: 'พ่อค้าที่ฉลาดจะไม่ซื้อของในราคาแพงเด็ดขาด กฎนี้จะหยุดการติดดอยของคุณตลอดกาล',
    summary: [
      'Fibonacci Retracement คือ เลขค่าเฉลี่ยสัดส่วนทองคำ ใช้ค้นหาพื้นที่พักราคา (หน้า 106)',
      'ระดับ 0.50 (Equilibrium) คือจุดกึ่งกลางแบ่งสภาวะตลาดเป็น 2 ส่วน',
      'Premium Zone (เหนือ 0.50): คือโซนของแพง เหมาะสำหรับการ "ขายหรือ Sell เท่านั้น" (หน้า 110)',
      'Discount Zone (ใต้ 0.50): คือโซนของถูก เหมาะสำหรับการ "ซื้อหรือ Buy เท่านั้น" (หน้า 111)',
      'กฎเหล็ก: ห้าม Buy ใน Premium Zone และห้าม Sell ใน Discount Zone เด็ดขาด'
    ],
    keyTerms: [
      { term: 'Equilibrium (0.50)', meaning: 'จุดสมดุลกึ่งกลางของสวิงราคา' },
      { term: 'Premium Zone', meaning: 'โซนราคาที่อยู่เหนือ 50% ถือเป็นของแพง เหมาะสำหรับฝั่ง Sell' },
      { term: 'Discount Zone', meaning: 'โซนราคาที่อยู่ต่ำกว่า 50% ถือเป็นของถูก เหมาะสำหรับฝั่ง Buy' },
      { term: 'OTE (Optimal Trade Entry)', meaning: 'บริเวณสัดส่วนทองคำ 0.618 - 0.79 ของ Fibonacci' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_106.png',
        caption: 'หน้า 106: นิยาม Fibonacci Retracement ค้นหาพื้นที่พักราคา',
        page: 106
      },
      {
        url: '/extracted/page_renders/page_109.png',
        caption: 'หน้า 109: Fibo Premium Discount ช่วยเลือกโซนของถูกของแพง',
        page: 109
      },
      {
        url: '/extracted/page_renders/page_110.png',
        caption: 'หน้า 110: มี OB ในโซน Premium (ของแพง) เหมาะกับการ Sell',
        page: 110
      },
      {
        url: '/extracted/page_renders/page_111.png',
        caption: 'หน้า 111: มี OB ในโซน Discount (ของถูก) เหมาะกับการ Buy',
        page: 111
      }
    ],
    lessons: [
      {
        id: 'lesson-15-1',
        title: 'หลักการแบ่งโซนของถูกของแพง (Premium vs Discount)',
        content: `จากหน้า 106-111 ของ E-Book:

**ตรรกะเบื้องหลัง Premium / Discount (หน้า 109):**
ในชีวิตจริง ไม่มีใครอยากซื้อสินค้าในราคาแพง และไม่มีใครอยากขายสินค้าในราคาถูก แต่ทำไมในตลาด Forex เทรดเดอร์จำนวนมากถึงชอบไล่ราคา Buy ตอนที่กราฟพุ่งขึ้นไปสูงแล้ว?

**วิธีใช้ Fibonacci กรองโซน (หน้า 110-111):**
1. ลาก Fibo จากจุด Swing Low ไปยัง Swing High (ในขาขึ้น) หรือจาก Swing High ไปยัง Swing Low (ในขาลง)
2. ดูเส้นกึ่งกลาง **0.50 (Equilibrium)**:
   - **เหนือ 0.50 (Premium Zone):** เป็นโซนของแพง หากมี Order Block หรือ Supply Zone อยู่ในโซนนี้ จะมีความน่าสนใจในการ **เปิดคำสั่ง SELL** (หน้า 110)
   - **ใต้ 0.50 (Discount Zone):** เป็นโซนของถูก หากมี Order Block หรือ Demand Zone อยู่ในโซนนี้ จะมีความน่าสนใจในการ **เปิดคำสั่ง BUY** (หน้า 111)`,
        corePrinciples: [
          'Buy ในโซน Discount (ใต้ 50%) เสมอ',
          'Sell ในโซน Premium (เหนือ 50%) เสมอ',
          'ถ้า OB อยู่ผิดโซน (เช่น Demand อยู่ใน Premium) ให้ตัดทิ้งทันที'
        ],
        practicalExamples: 'กรอบราคาสวิงทองคำอยู่ที่ 2300 ถึง 2400 จุดกึ่งกลาง 50% คือ 2350 หากราคาพักตัวลงมาอยู่ที่ 2370 ซึ่งยังอยู่ใน Premium Zone เราจะไม่ Buy จนกว่าราคาจะย่อลงมาต่ำกว่า 2350 (เช่น 2330 ใน Discount Zone) ร่วมกับ Demand Zone',
        proTips: 'โซน OTE (Optimal Trade Entry) ที่ระดับ 0.618 - 0.786 ภายใน Discount Zone คือจุดที่ให้ความคุ้มค่าของ R:R สูงที่สุดในโลกการเทรด',
        pitfalls: 'ไล่ราคา Buy ตามอารมณ์ FOMO ในโซน Premium สุดท้ายติดดอยเพราะสถาบันเทขายทำกำไร'
      }
    ],
    quiz: [
      {
        id: 'q15-1',
        type: 'mcq',
        question: 'ตามหน้า 110-111 ของ E-Book หากเราต้องการหาจังหวะเปิดคำสั่ง "BUY" เราควรเลือก Order Block ที่ตั้งอยู่ในโซนใดของ Fibonacci?',
        options: [
          'โซน Premium (เหนือระดับ 0.50 ขึ้นไป)',
          'โซน Discount (ต่ำกว่าระดับ 0.50 ลงมา)',
          'ที่ระดับ 0.00 พอดี',
          'โซนไหนก็ได้ไม่มีผลต่อความได้เปรียบ'
        ],
        correctIndex: 1,
        explanation: 'หน้า 111 ระบุว่า "มี OB ในโซน discount หรือโซนของถูก ทำให้เหมาะกับการซื้อหรือ Buy นั่นเอง"',
        referenceConcept: 'E-Book หน้า 111: Discount Zone Buying'
      }
    ]
  },
  {
    id: 'ch-16-psychology-model-entry',
    chapterNumber: 16,
    title: 'Mindset & Model Entry (จิตวิทยาและระบบเทรดสมบูรณ์)',
    englishTitle: 'Trading Psychology & Step-by-Step Complete Entry Blueprint',
    category: 'Mastery',
    difficulty: 'Advanced',
    estimatedMinutes: 30,
    pdfPages: '112 - 116',
    shortDescription: 'จิตวิทยาการยอมรับความผิดพลาด และพิมพ์เขียวระบบเทรด SMC เต็มรูปแบบตั้งแต่ HTF จนถึงกดส่งคำสั่ง',
    whyItMatters: 'เทคนิคที่ยอดเยี่ยมจะไร้ค่าหากปราศจากวินัยและแผนที่ชัดเจน บทนี้คือบทสรุปที่จะเปลี่ยนคุณเป็นนักล่าในตลาด',
    summary: [
      'Mindset (หน้า 112): "ใช่มันเหนื่อย ใช่มันผิดพลาด ใครสน? จงยอมรับทุกความผิดพลาดเก็บเป็นประสบการณ์ อย่าเร่งรีบ แค่ชนะตัวเองได้ก็ดีมากแล้ว"',
      'Model Entry Step 1: วิเคราะห์ Timeframe ใหญ่ (H4/H1) หา Trend และตีกรอบ POI (OB + FVG) ใน Discount/Premium',
      'Model Entry Step 2: รอให้ราคาเดินทางมาแตะ POI อย่างใจเย็น',
      'Model Entry Step 3: สลับไป Low Timeframe (M15/M5/M1) รอให้เกิด CHoCH หรือ MSS พร้อมการ Sweep Liquidity',
      'Model Entry Step 4: รอให้ราคาเคลียร์ IDM ย่อย แล้วเข้าออเดอร์ที่ Unmitigated OB หรือ SCOB',
      'Model Entry Step 5: คำนวณความเสี่ยง (Risk Management) วาง SL หลังสวิง และ TP ที่ BSL/SSL ฝั่งตรงข้าม (R:R 1:3+)'
    ],
    keyTerms: [
      { term: 'Multi-Timeframe Analysis', meaning: 'การผสานกรอบเวลาใหญ่ (HTF) หาแนวโน้ม กับกรอบเวลาเล็ก (LTF) หาจุดเข้า' },
      { term: 'Model Entry', meaning: 'พิมพ์เขียวขั้นตอนปฏิบัติการเทรดที่ทำซ้ำได้ตามกฎ 100%' },
      { term: 'Risk Management', meaning: 'การบริหารความเสี่ยง กำหนดขาดทุนไม่เกิน 1-2% ต่อไม้' },
      { term: 'Trading Psychology', meaning: 'การควบคุมอารมณ์ วินัย และความอดทนในการรอคอยสัญญาณเทรด' }
    ],
    originalImages: [
      {
        url: '/extracted/page_renders/page_112.png',
        caption: 'หน้า 112: ข้อคิดและ Mindset ของเทรดเดอร์ (ใช่มันเหนื่อย ใช่มันผิดพลาด ใครสน?)',
        page: 112
      },
      {
        url: '/extracted/page_renders/page_113.png',
        caption: 'หน้า 113: Model Entry พิมพ์เขียวที่ 1 โครงสร้างภาพรวมและจุดเข้าเทรด',
        page: 113
      },
      {
        url: '/extracted/page_renders/page_114.png',
        caption: 'หน้า 114: Model Entry พิมพ์เขียวที่ 2 การ Confirm ใน Low Timeframe',
        page: 114
      },
      {
        url: '/extracted/page_renders/page_115.png',
        caption: 'หน้า 115: Model Entry พิมพ์เขียวที่ 3 การวาง Stop Loss และ Take Profit ตาม R:R',
        page: 115
      },
      {
        url: '/extracted/page_renders/page_116.png',
        caption: 'หน้า 116: ปกหลัง SMC WARRIORS TRADER',
        page: 116
      }
    ],
    lessons: [
      {
        id: 'lesson-16-1',
        title: 'จิตวิทยาของ SMC Warrior: ยอมรับความผิดพลาดและชนะตัวเอง',
        content: `จากหน้า 112 ของ E-Book:

**"ใช่มันเหนื่อย ใช่มันผิดพลาด ใครสน?"**
**"จงกลับมาเหนื่อยให้มากกว่านี้ จงกลับมาผิดพลาดให้มากกว่านี้ จงปรับปรุงแล้วแก้ไข ยอมรับทุกความผิดพลาดเก็บเป็นประสบการณ์"**
**"ทุกความผิดพลาดสอนให้เราอย่าทำพลาดอีก อย่าเร่งรีบที่จะเป็นคนที่ประสบความสำเร็จ ค่อยๆ เป็นค่อยๆ ไป ความพยายามและความต่อเนื่องจะส่งผลให้กับเราในสักวัน อย่าไปเปรียบกับใคร แค่ชนะตัวเองได้ ก็ดีมากแล้ว"**

**ข้อคิดสำคัญสำหรับเทรดเดอร์:**
1. การขาดทุน (Loss) เป็นส่วนหนึ่งของธุรกิจการเทรด ไม่มีใครมี Win Rate 100%
2. สิ่งที่แยกนักเทรดมืออาชีพออกจากมือสมัครเล่น คือการมี **วินัยในการคุม Risk Management** เมื่อผิดทางตัดขาดทุนตามแผน ไม่แก้มือ (Revenge Trading)
3. โฟกัสที่การทำตามกระบวนการ (Process) ที่ถูกต้อง ไม่ใช่โฟกัสที่ผลลัพธ์ของไม้เดียว`,
        corePrinciples: [
          'ยอมรับความผิดพลาดเป็นค่าหน่วยกิตในตลาด',
          'ความสม่ำเสมอชนะความโลภในระยะยาว',
          'แข่งกับตัวเองในอดีต อย่าเปรียบเทียบพอร์ตกับใครในโซเชียล'
        ],
        practicalExamples: 'หากเทรดแพ้ 2 ไม้ติด ให้ปิดหน้าจอ เดินออกไปสูดอากาศ และกลับมาทบทวน Journal ว่าเราผิดกฎข้อไหนใน 5 สเต็ปของ Model Entry หรือไม่',
        proTips: 'จดบันทึกการเทรด (Trading Journal) ทุกไม้ เพื่อดูว่าเราพัฒนาขึ้นจากเดือนที่แล้วอย่างไร',
        pitfalls: 'เทรดโอเวอร์ล็อตหวังรวยเร็วในไม้เดียว ซึ่งจบลงด้วยการล้างพอร์ตเสมอ'
      },
      {
        id: 'lesson-16-2',
        title: 'พิมพ์เขียว 5 สเต็ป Model Entry สไตล์สถาบัน',
        content: `จากหน้า 113-115 ของ E-Book สรุประบบการเทรดแบบครบวงจร:

**สเต็ปที่ 1 (HTF Analysis - แผนที่ใหญ่):**
- เปิดกราฟ Timeframe H4 หรือ H1
- ระบุ Trend หลัก (HH/HL หรือ LH/LL)
- มาร์กจุด POI ที่สำคัญ: หา Unmitigated OB + FVG ที่อยู่ในโซน **Discount (สำหรับ Buy)** หรือ **Premium (สำหรับ Sell)**

**สเต็ปที่ 2 (Patience - ความอดทน):**
- ตั้ง Alert ไว้ที่ขอบโซน POI
- นั่งรอให้ราคาเดินทางเข้ามาทดสอบ ห้ามไล่ราคาเด็ดขาด

**สเต็ปที่ 3 (LTF Confirmation - ยืนยันในไทม์เฟรมเล็ก):**
- เมื่อราคาแตะ POI สลับไปดู Timeframe M5 หรือ M1
- รอให้ราคาทำ **CHoCH หรือ MSS** เพื่อยืนยันว่าสถาบันเริ่มกลับทิศทางจริง
- สังเกตการเกิด **Liquidity Sweep** ที่ชัดเจน

**สเต็ปที่ 4 (Entry Execution - การเข้าทำ):**
- รอให้ราคาย่อตัวมาเคลียร์ **IDM ย่อย** ใน M5
- ตั้ง Limit Order ที่ **Order Block (OB) ย่อย** หรือรอแท่ง **SCOB** ยืนยันปิดเนื้อคลุมไส้

**สเต็ปที่ 5 (Trade Management - ปิดประตูแพ้):**
- วาง **Stop Loss (SL)** ไว้หลังสวิงของแท่ง SCOB หรือหลัง Low/High สำคัญ
- วาง **Take Profit (TP)** ที่จุด Liquidity ฝั่งตรงข้าม (BSL สำหรับ Buy / SSL สำหรับ Sell)
- คำนวณ R:R ให้ได้อย่างน้อย **1:3 ถึง 1:5 ขึ้นไป**`,
        corePrinciples: [
          'HTF กำหนดทิศทาง (Trend & POI)',
          'LTF คอนเฟิร์มจุดเข้า (CHoCH, IDM, SCOB)',
          'R:R ต้องคุ้มค่าเสมอ (1:3+)'
        ],
        practicalExamples: 'วิเคราะห์ทอง H1 เห็น POI Demand ที่ 2320 เมื่อราคาลงมาแตะ ใน M5 เกิด CHoCH ทะลุ 2325 แล้วย่อเคลียร์ IDM ที่ 2322 เข้า Buy ที่ OB 2321 SL 2318 (เสี่ยง 30 จุด) TP ที่ BSL ยอดเดิม 2336 (กำไร 150 จุด) ได้ R:R สูงถึง 1:5!',
        proTips: 'เมื่อราคาเดินทางไปได้ระยะ 1:1 หรือ 1:2 ให้เลื่อน SL มากันทุน (Break-Even) เพื่อให้การเทรดนั้นไม่มีความเสี่ยงหลงเหลืออยู่อีกต่อไป',
        pitfalls: 'เทรดแบบไร้แผน เข้าออเดอร์ตามอารมณ์โดยไม่ผ่านการเช็กลิสต์ทั้ง 5 ขั้นตอน'
      }
    ],
    quiz: [
      {
        id: 'q16-1',
        type: 'scenario',
        question: 'ในขั้นตอน Model Entry ตามหน้า 113-115 เมื่อราคาใน Timeframe ใหญ่ (HTF) เดินทางมาแตะโซน POI แล้ว ขั้นตอนถัดไปที่ถูกต้องคืออะไร?',
        options: [
          'กดเปิดออเดอร์เต็ม Lot ทันทีไม่ต้องรอ',
          'สลับไป Low Timeframe (LTF) รอให้เกิดสัญญาณ Confirm เช่น CHoCH/MSS และการเคลียร์ IDM หรือแท่ง SCOB ก่อนเข้าทำ',
          'รีบปิดออเดอร์ที่มีอยู่ทั้งหมดและถอนเงิน',
          'รอให้ราคาผ่านโซนไป 200 จุดก่อนค่อยตาม'
        ],
        correctIndex: 1,
        explanation: 'หน้า 113-115 แสดงขั้นตอนการเทรดแบบ Multi-Timeframe เมื่อแตะ POI ใน HTF ต้องรอการยืนยันใน LTF ด้วย CHoCH/IDM เพื่อให้ได้ Stop Loss ที่แคบและลดความเสี่ยง',
        referenceConcept: 'E-Book หน้า 113-115: Model Entry Blueprint'
      },
      {
        id: 'q16-2',
        type: 'mcq',
        question: 'ตามหน้า 112 ในเรื่อง Mindset สิ่งสำคัญที่สุดที่เทรดเดอร์ควรมีคืออะไร?',
        options: [
          'การพยายามเทรดให้ไม่แพ้เลยแม้แต่ไม้เดียว',
          'การยอมรับทุกความผิดพลาดเป็นประสบการณ์ อดทนต่อเนื่อง ไม่เร่งรีบ และมุ่งเน้นการชนะตัวเอง',
          'การซื้อคอร์สและอินดิเคเตอร์ลับราคาแพง',
          'การเปรียบเทียบผลกำไรกับคนอื่นทุกวัน'
        ],
        correctIndex: 1,
        explanation: 'หน้า 112 เน้นย้ำว่า "ยอมรับทุกความผิดพลาดเก็บเป็นประสบการณ์... อย่าเร่งรีบที่จะเป็นคนที่ประสบความสำเร็จ ค่อยๆเป็นค่อยๆไป... แค่ชนะตัวเองได้ก็ดีมากแล้ว"',
        referenceConcept: 'E-Book หน้า 112: Trading Mindset'
      }
    ]
  }
]

export const GLOSSARY_TERMS: GlossaryTerm[] = [
  {
    id: 'g-smart-money',
    term: 'Smart Money (SMC)',
    thaiName: 'เงินฉลาด / สถาบันการเงินรายใหญ่',
    category: 'Foundations',
    definition: 'กลุ่มผู้เล่นรายใหญ่ในตลาด เช่น ธนาคารกลาง ธนาคารเพื่อการลงทุน และกองทุนเฮดจ์ฟันด์ ที่มีปริมาณเงินมหาศาลพอที่จะกำหนดทิศทางของกราฟได้',
    example: 'การทุบกราฟลง 100 จุดแล้วดึงกลับทันทีเพื่อกินสภาพคล่อง เป็นพฤติกรรมคลาสสิกของ Smart Money',
    relatedChapterId: 'ch-01-forex-basics'
  },
  {
    id: 'g-retail-trader',
    term: 'Retail Trader',
    thaiName: 'เทรดเดอร์รายย่อย',
    category: 'Foundations',
    definition: 'ประชากรทั่วไปที่มีจำนวนคนมากที่สุดในตลาด Forex แต่ถือครองเม็ดเงินน้อยมาก ไม่มีผลต่อการขยับของกราฟ',
    example: 'รายย่อยมักตั้ง Stop Loss ไว้หลังแนวรับแนวต้านแบบดั้งเดิม ทำให้ตกเป็นเหยื่อของการ Sweep Liquidity',
    relatedChapterId: 'ch-01-forex-basics'
  },
  {
    id: 'g-base-currency',
    term: 'Base Currency',
    thaiName: 'สกุลเงินหลัก (ตัวหน้า)',
    category: 'Foundations',
    definition: 'สกุลเงินที่อยู่ข้างหน้าของคู่เงิน มีค่าเท่ากับ 1 เสมอ เช่น EUR ในคู่ EUR/USD หรือ USD ในคู่ USD/JPY',
    example: 'USD/THB = 36.80 หมายถึง 1 USD (Base) แลกได้ 36.80 บาทไทย',
    relatedChapterId: 'ch-01-forex-basics'
  },
  {
    id: 'g-quote-currency',
    term: 'Quote Currency',
    thaiName: 'สกุลเงินอ้างอิง (ตัวหลัง)',
    category: 'Foundations',
    definition: 'สกุลเงินที่อยู่ข้างหลัง ใช้แสดงมูลค่าเปรียบเทียบกับ 1 หน่วยของสกุลเงินตัวหน้า หากตัวหลังแข็งค่าขึ้น กราฟจะปรับตัวลง',
    example: 'เมื่อเงิน JPY แข็งค่าขึ้น กราฟคู่ USD/JPY จะปรับตัวลงอย่างรวดเร็ว',
    relatedChapterId: 'ch-01-forex-basics'
  },
  {
    id: 'g-market-structure',
    term: 'Market Structure',
    thaiName: 'โครงสร้างตลาด',
    category: 'Structure',
    definition: 'แบบแผนการเคลื่อนไหวของราคาที่ประกอบด้วยสวิง High และ Low ใน 3 สภาวะ: ขาขึ้น ขาลง และไซด์เวย์',
    example: 'การอ่านโครงสร้างช่วยบอกว่าควรโฟกัสฝั่ง Buy หรือ Sell',
    relatedChapterId: 'ch-02-market-structure'
  },
  {
    id: 'g-higher-high',
    term: 'Higher High (HH)',
    thaiName: 'จุดสูงสุดที่ยกตัวสูงขึ้น',
    category: 'Structure',
    definition: 'จุดยอดสวิงใหม่ที่ทำราคาสูงกว่าจุดยอดสวิงก่อนหน้า เป็นสัญญาณหลักของ Up Trend',
    example: 'ราคาปิดแท่งเหนือยอดเดิม 2000 ไปทำยอดที่ 2020 เกิดเป็น HH',
    relatedChapterId: 'ch-02-market-structure'
  },
  {
    id: 'g-higher-low',
    term: 'Higher Low (HL)',
    thaiName: 'จุดต่ำสุดที่ยกฐานสูงขึ้น',
    category: 'Structure',
    definition: 'จุดก้นสวิงใหม่ที่ย่อตัวลงมาแต่ไม่หลุดก้นสวิงก่อนหน้า เป็นฐานรับใน Up Trend',
    example: 'ราคาย่อตัวลงมาที่ 1980 สูงกว่าฐานเดิมที่ 1950 เกิดเป็น HL',
    relatedChapterId: 'ch-02-market-structure'
  },
  {
    id: 'g-demand-zone',
    term: 'Demand Zone',
    thaiName: 'โซนอุปสงค์ (โซนซื้อ)',
    category: 'Foundations',
    definition: 'บริเวณที่มีความต้องการซื้อหนาแน่น เมื่อราคาลงมาถึงจะมีแรงผลักดันให้พุ่งขึ้น มีรูปแบบ DBR และ RBR',
    example: 'ราคาลงมาแตะ Demand DBR แล้วเกิดแท่งเขียวพุ่งขึ้น 50 จุด',
    relatedChapterId: 'ch-03-demand-supply'
  },
  {
    id: 'g-supply-zone',
    term: 'Supply Zone',
    thaiName: 'โซนอุปทาน (โซนขาย)',
    category: 'Foundations',
    definition: 'บริเวณที่มีความต้องการขายหนาแน่น เมื่อราคาขึ้นมาถึงจะมีแรงเทขายกดให้ร่วงลง มีรูปแบบ RBD และ DBD',
    example: 'ราคาขึ้นมาชน Supply RBD แล้วทิ้งตัวลงทันที',
    relatedChapterId: 'ch-03-demand-supply'
  },
  {
    id: 'g-impulse-wave',
    term: 'Impulse Wave',
    thaiName: 'คลื่นส่งหลัก',
    category: 'Structure',
    definition: 'คลื่นขยายที่มีความรุนแรงและรวดเร็ว เดินทางตามทิศทางของแนวโน้มหลัก เกิดจากการเข้าทำของสถาบัน',
    example: 'แท่งเขียวยาว 3 แท่งติดพุ่งทะลุ 100 จุดใน 15 นาที',
    relatedChapterId: 'ch-04-impulse-pullback'
  },
  {
    id: 'g-pullback-wave',
    term: 'Pullback Wave',
    thaiName: 'คลื่นพักตัว',
    category: 'Structure',
    definition: 'คลื่นย่อยที่พักตัวสวนทางกับเทรนหลัก เคลื่อนที่ช้า มีแท่งเทียนซ้อนทับกันมาก เป็นช่วงสะสมสภาพคล่อง',
    example: 'ราคาย่อยิบตาลงมา 8 แท่งแต่ลงมาเพียง 20 จุด',
    relatedChapterId: 'ch-04-impulse-pullback'
  },
  {
    id: 'g-valid-pullback',
    term: 'Valid Pullback',
    thaiName: 'การพักราคาที่ถูกต้อง',
    category: 'Structure',
    definition: 'การพักตัวที่แท่งถัดไปสามารถเบรค/กวาด Low (ในขาขึ้น) หรือ High (ในขาลง) ของแท่งสูงสุด/ต่ำสุดของรอบได้สำเร็จ',
    example: 'แท่งที่ 2 มีไส้เทียนแลบกิน Low ของแท่งสูงสุด ทำให้เกิด Valid Pullback ทันที',
    relatedChapterId: 'ch-05-valid-pullback'
  },
  {
    id: 'g-bos',
    term: 'BOS (Break of Structure)',
    thaiName: 'การเบรคโครงสร้างตามเทรน',
    category: 'Structure',
    definition: 'การที่ราคาเดินทางตามแนวโน้มเดิมและสามารถ "ปิดเนื้อเทียน" ทะลุ High หรือ Low สำคัญได้เพื่อยืนยันการไปต่อ',
    example: 'แท่ง H1 ปิดเนื้อเทียนเต็มแท่งเหนือสวิง High ก่อนหน้า ยืนยันการเกิด BOS',
    relatedChapterId: 'ch-06-bos-break-of-structure'
  },
  {
    id: 'g-idm',
    term: 'IDM (Inducement)',
    thaiName: 'จุดล่อซื้อขาย (กับดักสถาบัน)',
    category: 'Liquidity',
    definition: 'สวิง Valid Pullback แรกที่อยู่ใกล้ราคาปัจจุบันที่สุด สถาบันสร้างขึ้นเพื่อล่อรายย่อย เมื่อถูกเคลียร์จะคอนเฟิร์ม High/Low ทันที',
    example: 'ราคาทุบลงมากวาด IDM สำเร็จ ทำให้ยอดดอยด้านบนได้รับการคอนเฟิร์มเป็น Higher High',
    relatedChapterId: 'ch-07-idm-inducement'
  },
  {
    id: 'g-choch',
    term: 'CHoCH (Change of Character)',
    thaiName: 'การเปลี่ยนทิศทางโครงสร้าง',
    category: 'Structure',
    definition: 'สัญญาณแรกของการเปลี่ยนแนวโน้ม เกิดขึ้นเมื่อราคาปิดเนื้อเทียนทะลุ Major Low (ในขาขึ้น) หรือ Major High (ในขาลง)',
    example: 'แท่งเทียนปิดเนื้อต่ำกว่า Low ล่าสุด เปลี่ยนโครงสร้างจาก Up Trend สู่ Down Trend',
    relatedChapterId: 'ch-09-choch-mss'
  },
  {
    id: 'g-mss',
    term: 'MSS (Market Structure Shift)',
    thaiName: 'การเปลี่ยนโครงสร้างเฉียบพลัน',
    category: 'Structure',
    definition: 'การกลับตัวอย่างรวดเร็วในกรอบเวลาย่อยหลังราคาชน POI ใช้ยืนยันจุดเข้าออเดอร์',
    example: 'ใน M5 เกิด MSS หลังราคาสัมผัส Demand Zone H1',
    relatedChapterId: 'ch-09-choch-mss'
  },
  {
    id: 'g-bsl',
    term: 'BSL (Buy Side Liquidity)',
    thaiName: 'สภาพคล่องฝั่งซื้อ',
    category: 'Liquidity',
    definition: 'กลุ่มคำสั่ง Buy Stop และ Stop Loss ของฝั่ง Sell ที่สะสมอยู่เหนือจุด High หรือ Equal Highs',
    example: 'ราคากระชากขึ้นไปกิน BSL เหนือแนวต้านแล้วทิ้งตัวลงอย่างรวดเร็ว',
    relatedChapterId: 'ch-10-liquidity-bsl-ssl'
  },
  {
    id: 'g-ssl',
    term: 'SSL (Sell Side Liquidity)',
    thaiName: 'สภาพคล่องฝั่งขาย',
    category: 'Liquidity',
    definition: 'กลุ่มคำสั่ง Sell Stop และ Stop Loss ของฝั่ง Buy ที่สะสมอยู่ใต้จุด Low หรือ Equal Lows',
    example: 'ราคาทุบลงไปกิน SSL ใต้แนวรับคู่ EQL ก่อนพุ่งขึ้นทำ New High',
    relatedChapterId: 'ch-10-liquidity-bsl-ssl'
  },
  {
    id: 'g-order-flow',
    term: 'Order Flow (OF)',
    thaiName: 'การไหลของคำสั่งซื้อขายสถาบัน',
    category: 'Entry Execution',
    definition: 'แรงซื้อสุดท้ายก่อนลง หรือแรงขายสุดท้ายก่อนขึ้น ใช้ได้เพียง 1 ครั้งเท่านั้น (Single-Use Rule)',
    example: 'เมื่อราคาลงมาทดสอบ OF ครั้งแรกแล้วดีดขึ้น การกลับมาครั้งที่สองจะไม่มีการเข้าเทรดซ้ำ',
    relatedChapterId: 'ch-11-order-flow-of'
  },
  {
    id: 'g-order-block',
    term: 'Order Block (OB)',
    thaiName: 'บล็อกคำสั่งสถาบัน',
    category: 'Entry Execution',
    definition: 'แท่งเทียนแท่งสุดท้ายก่อนเกิด Impulse Move ที่กวาด Liquidity และสร้าง FVG ใช้เป็นจุดเปิดออเดอร์',
    example: 'ตั้ง Buy Limit ที่กรอบ Bullish OB พร้อม Stop Loss ใต้แท่ง OB',
    relatedChapterId: 'ch-12-order-blocks-scob'
  },
  {
    id: 'g-scob',
    term: 'SCOB (Single Candle OB)',
    thaiName: 'บล็อกคำสั่งแท่งเดี่ยวคอนเฟิร์ม',
    category: 'Entry Execution',
    definition: 'เทคนิคการเข้าเทรดด้วยแท่งเทียนแท่งเดียวหลังแตะ POI โดยแท่งแรกกวาด High/Low และแท่งถัดไปปิดเนื้อคลุมไส้',
    example: 'เกิด Bullish SCOB ใน M5 ช่วยให้ได้ Stop Loss เพียง 6 จุด และ R:R 1:8',
    relatedChapterId: 'ch-12-order-blocks-scob'
  },
  {
    id: 'g-breaker-block',
    term: 'BRK (Breaker Block)',
    thaiName: 'บล็อกพลิกกลับ (Flip Zone)',
    category: 'Entry Execution',
    definition: 'Order Block ที่ถูกราคาเบรคทะลุครั้งเดียว แล้วกลับมาทำหน้าที่สลับขั้วจาก Demand เป็น Supply หรือกลับกัน',
    example: 'Demand ที่ถูกทะลุเปลี่ยนเป็น BRK Supply เมื่อราคาย้อนกลับมาให้เปิด Sell',
    relatedChapterId: 'ch-13-breaker-block-bb-brk'
  },
  {
    id: 'g-poi',
    term: 'POI (Point of Interest)',
    thaiName: 'จุดที่มีนัยสำคัญสูงสุด',
    category: 'Entry Execution',
    definition: 'โซนเป้าหมายที่มีการทับซ้อนกันของหลายเงื่อนไข (Confluence) เช่น HTF OB + FVG + Liquidity',
    example: 'กำหนด POI ไว้ที่ 2350 แล้วรอการคอนเฟิร์มใน LTF ก่อนเข้าเทรด',
    relatedChapterId: 'ch-14-poi-fvg'
  },
  {
    id: 'g-fvg',
    term: 'FVG (Fair Value Gap)',
    thaiName: 'ช่องว่างราคาที่ไม่สมดุล',
    category: 'Entry Execution',
    definition: 'ช่องว่างระหว่างไส้เทียนของแท่งที่ 1 และแท่งที่ 3 จากการเคลื่อนที่รวดเร็วของแท่งที่ 2 เป็นจุดที่ราคามักกลับมาเติมเต็ม',
    example: 'ราคาย่อตัวลงมาปิดช่องว่าง FVG แล้วดีดตัวพุ่งขึ้นต่อไปตามเทรนเดิม',
    relatedChapterId: 'ch-14-poi-fvg'
  },
  {
    id: 'g-equilibrium',
    term: 'Equilibrium (0.50)',
    thaiName: 'จุดสมดุลราคา',
    category: 'Entry Execution',
    definition: 'ระดับ 50% ของ Fibonacci ที่แบ่งสภาวะตลาดออกเป็นฝั่ง Premium และ Discount',
    example: 'ใช้เส้น 0.50 ตัดสินใจว่าจะมองหาหน้า Buy หรือหน้า Sell',
    relatedChapterId: 'ch-15-fibonacci-premium-discount'
  },
  {
    id: 'g-premium-zone',
    term: 'Premium Zone',
    thaiName: 'โซนของแพง',
    category: 'Entry Execution',
    definition: 'พื้นที่ราคาเหนือระดับ 50% ของ Fibonacci เหมาะสำหรับการมองหาจังหวะเปิดคำสั่ง SELL เท่านั้น',
    example: 'หา Bearish OB ที่ตั้งอยู่ในโซน Premium เพื่อเปิดออเดอร์ Sell',
    relatedChapterId: 'ch-15-fibonacci-premium-discount'
  },
  {
    id: 'g-discount-zone',
    term: 'Discount Zone',
    thaiName: 'โซนของถูก',
    category: 'Entry Execution',
    definition: 'พื้นที่ราคาต่ำกว่าระดับ 50% ของ Fibonacci เหมาะสำหรับการมองหาจังหวะเปิดคำสั่ง BUY เท่านั้น',
    example: 'หา Bullish OB ที่ตั้งอยู่ในโซน Discount เพื่อเปิดออเดอร์ Buy',
    relatedChapterId: 'ch-15-fibonacci-premium-discount'
  },
  {
    id: 'g-risk-reward',
    term: 'Risk to Reward Ratio (R:R)',
    thaiName: 'อัตราผลตอบแทนต่อความเสี่ยง',
    category: 'Mastery',
    definition: 'สัดส่วนระหว่างจำนวนเงินที่ยอมขาดทุน (Risk) กับจำนวนเงินที่คาดหวังจะได้กำไร (Reward) ในระบบ SMC มักตั้งเป้า 1:3 ขึ้นไป',
    example: 'เสี่ยง 10 ดอลลาร์เพื่อหวังกำไร 50 ดอลลาร์ คิดเป็น R:R 1:5',
    relatedChapterId: 'ch-16-psychology-model-entry'
  }
]

export const PRACTICAL_SCENARIOS: Scenario[] = [
  {
    id: 'sim-1-idm-confirmation',
    title: 'สถานการณ์ที่ 1: การเลือกระดับ IDM เพื่อคอนเฟิร์ม Higher High',
    category: 'IDM & Structure',
    difficulty: 'Intermediate',
    setupDescription: 'ราคาทองคำ XAUUSD ใน Timeframe H1 พุ่งขึ้นทำยอดดอยที่ 2350 จากนั้นมีการย่อตัวลงมาสร้างสวิง 2 จุด: จุด A (ย่อสั้นๆ ไม่หลุด Low แท่งสูงสุด) และจุด B (ย่อตัวหลุด Low แท่งสูงสุด เกิดเป็น Valid Pullback แรกที่ราคา 2330) ต่อมาราคาพุ่งต่อไปที่ 2360',
    chartRenderUrl: '/extracted/page_renders/page_039.png',
    originalPageRef: 39,
    question: 'หากคุณต้องการยืนยันว่ายอด 2360 ได้รับการคอนเฟิร์มเป็น Higher High ที่แท้จริง ราคาจะต้องถอยกลับมาเคลียร์จุดใด?',
    options: [
      {
        id: 'opt-a',
        text: 'จุด A เพราะเป็นจุดที่ย่อตัวลงมาจุดแรกสุดบนหน้าจอ',
        isCorrect: false,
        feedback: 'ไม่ถูกต้อง! จุด A ไม่ใช่ Valid Pullback ตามกฎแท่งเทียนหน้า 25 และ 35 จุดที่ไม่ใช่ Valid Pullback จะไม่สามารถนับเป็น IDM ได้'
      },
      {
        id: 'opt-b',
        text: 'จุด B (2330) เพราะเป็นจุดต่ำสุดของ Valid Pullback แรกที่ถูกต้องตามเงื่อนไข E-Book',
        isCorrect: true,
        feedback: 'ถูกต้องยอดเยี่ยม! ตามหน้า 34 และ 39 ของ E-Book IDM คือจุดต่ำสุดของ Valid Pullback แรก เมื่อราคาถอยมากวาดจุด B ยอด 2360 จึงจะได้รับการคอนเฟิร์มเป็น Higher High ทันที'
      },
      {
        id: 'opt-c',
        text: 'ไม่ต้องรอให้ย่อเคลียร์จุดใด ยอด 2360 คอนเฟิร์มทันทีที่จบแท่งเขียว',
        isCorrect: false,
        feedback: 'ผิดหลักการ SMC! หน้า 39 ระบุชัดเจนว่า High จะคอนเฟิร์มก็ต่อเมื่อ IDM ถูกเคลียร์แล้วเท่านั้น หากไม่เคลียร์ IDM จุด High จะยังไม่ได้รับการยืนยัน'
      }
    ],
    institutionalExplanation: 'Smart Money ใช้จุด B เป็นเหยื่อล่อสภาพคล่อง (Inducement) เพราะรายย่อยเห็นว่าจุด B เป็นแนวรับย่อย เมื่อราคากลับมากวาดจุด B จะกิน Stop Loss ของรายย่อยจนหมด ส่งผลให้ยอด 2360 ได้รับการบันทึกเป็น High แท้จริง'
  },
  {
    id: 'sim-2-wick-bos-transfer',
    title: 'สถานการณ์ที่ 2: แท่งเทียนแลบไส้ทะลุ High (Wick Break Trap)',
    category: 'BOS Mechanics',
    difficulty: 'Intermediate',
    setupDescription: 'คู่เงิน EUR/USD มี High สำคัญเดิมอยู่ที่ 1.0900 มีแท่งเทียนเขียวพุ่งทะลุขึ้นไปทำไส้ที่ 1.0920 แต่เมื่อจบแท่ง 1 ชั่วโมง เนื้อเทียนกลับทิ้งตัวลงมาปิดที่ระดับ 1.0890 (ต่ำกว่า High เดิม)',
    chartRenderUrl: '/extracted/page_renders/page_031.png',
    originalPageRef: 31,
    question: 'ตามกฎของ E-Book หน้า 30-31 ข้อใดคือการประเมินสถานการณ์ที่ถูกต้องที่สุด?',
    options: [
      {
        id: 'opt-1',
        text: 'เกิด BOS แล้วเรียบร้อย ให้กด Buy ตามทันที',
        isCorrect: false,
        feedback: 'อันตรายมาก! หน้า 30 ระบุว่า BOS ที่ถูกต้อง "ต้องถูกเบรคด้วยเนื้อเทียน" การใช้ไส้เทียนทะลุไม่ถือเป็น BOS'
      },
      {
        id: 'opt-2',
        text: 'ยังไม่เกิด BOS แต่จุด Higher High (HH) จะถูกเคลื่อนย้าย (Transfer) ไปที่ปลายไส้ 1.0920 แทน และต้องรอแท่งถัดไปปิดเนื้อเทียนทะลุ 1.0920',
        isCorrect: true,
        feedback: 'ถูกต้องแม่นยำ! หน้า 31 ของ E-Book ระบุว่า การเบรคด้วยไส้เทียน จุด HH จะถูกเคลื่อนย้ายไปยังบริเวณปลายไส้เทียน จนกว่าจะมีการเบรคด้วยเนื้อเทียน'
      },
      {
        id: 'opt-3',
        text: 'กราฟกลับตัวเป็นเทรนขาลงทันที ให้เปิด Sell ทันที',
        isCorrect: false,
        feedback: 'ยังเร็วเกินไปที่จะสรุปว่ากลับตัว โครงสร้างหลักยังคงเป็นขาขึ้น เพียงแค่ BOS ยังไม่สมบูรณ์เท่านั้น'
      }
    ],
    institutionalExplanation: 'การที่ราคาแทงไส้ทะลุ 1.0900 คือการที่ Smart Money กวาด Buy Side Liquidity (BSL) เหนือ High เดิม เพื่อเก็บของ ไม่ใช่การคอนเฟิร์มว่าเทรนจะวิ่งทะลุ การย้ายจุดอ้างอิงไปที่ 1.0920 จะป้องกันไม่ให้เราเข้าเทรดผิดจังหวะ'
  },
  {
    id: 'sim-3-order-flow-retest',
    title: 'สถานการณ์ที่ 3: กฎเหล็ก Order Flow (Single-Use Rule)',
    category: 'Order Flow',
    difficulty: 'Advanced',
    setupDescription: 'ราคาทองคำทิ้งตัวลงมาแตะ Order Flow (OF) ฝั่ง Buy ที่ราคา 2300 เป็นครั้งแรก และดีดตัวขึ้นไป 80 จุดตามคาด สองชั่วโมงถัดมาราคาทิ้งตัวลงมาทดสอบที่ระดับ 2300 เดิมอีกครั้งหนึ่ง',
    chartRenderUrl: '/extracted/page_renders/page_076.png',
    originalPageRef: 76,
    question: 'ในฐานะนักเทรด SMC Warriors คุณควรตัดสินใจอย่างไรในการทดสอบครั้งที่สองนี้?',
    options: [
      {
        id: 'opt-of-1',
        text: 'เปิด Buy ไม้ใหญ่ขึ้น เพราะแนวรับทดสอบซ้ำแปลว่าแข็งแกร่งมาก',
        isCorrect: false,
        feedback: 'ผิดหลักการอย่างรุนแรง! นั่นคือแนวคิดของแนวรับรายย่อย ซึ่งมักโดนทุบแตก'
      },
      {
        id: 'opt-of-2',
        text: 'ไม่เข้าเทรด Buy ที่โซนนี้เด็ดขาด เพราะตามหน้า 76 กฎเหล็กของ OF คือสามารถใช้ได้เพียง 1 ครั้งเท่านั้น ออเดอร์ถูก Mitigate ไปแล้ว',
        isCorrect: true,
        feedback: 'ถูกต้องระดับมืออาชีพ! หน้า 76 ระบุว่า "เงื่อนไขของ OF คือสามารถใช้ได้เพียง 1 ครั้งเท่านั้น จะไม่มีการเติมไม้ตอนที่ตลาดกลับมาทดสอบโซน"'
      },
      {
        id: 'opt-of-3',
        text: 'รอให้ราคาหลุดแล้วกด Sell ทันทีแบบไม่มีการรอรีเทสต์',
        isCorrect: false,
        feedback: 'การไล่ราคา Sell หลังหลุดโซนก็มีความเสี่ยงที่จะเจอไส้ Sweep Liquidity เช่นกัน ควรรอโครงสร้างใหม่'
      }
    ],
    institutionalExplanation: 'ในครั้งแรกที่ราคาแตะ 2300 สถาบันได้ทำการปิดไม้ขาดทุนและกวาดออเดอร์ไปหมดแล้ว (Mitigated) โซนนี้จึงกลวงเปล่า การกลับมาครั้งที่สองมักเป็นการทุบเพื่อทะลุไปหาโซนด้านล่างต่อไป'
  },
  {
    id: 'sim-4-scob-confirmation',
    title: 'สถานการณ์ที่ 4: การเข้าเทรดด้วย SCOB ที่กรอบ POI',
    category: 'Entry Execution',
    difficulty: 'Advanced',
    setupDescription: 'ราคา GBP/USD เดินทางขึ้นมาชน POI Supply Zone ใน H4 ที่ราคา 1.2750 ใน Timeframe M5 เกิดแท่งที่ 1 แทงไส้ทะลุ High ขึ้นไปที่ 1.2755 แล้วดึงไส้กลับลงมา แท่งที่ 2 ถัดมาทิ้งตัวลงมาปิดเนื้อเทียนต่ำกว่าเนื้อและไส้ล่างของแท่งที่ 1 อย่างชัดเจน',
    chartRenderUrl: '/extracted/page_renders/page_088.png',
    originalPageRef: 88,
    question: 'ลักษณะแท่งเทียนที่เกิดขึ้นนี้จัดเป็นรูปแบบใด และควรวางแผนเข้าเทรดอย่างไร?',
    options: [
      {
        id: 'opt-scob-1',
        text: 'เป็นรูปแบบ Inside Bar ให้รอต่อไปอีก 10 แท่ง',
        isCorrect: false,
        feedback: 'ไม่ถูกต้อง แท่งที่ 1 ได้ Sweep High ของแท่งก่อนหน้าไปแล้ว และแท่งที่ 2 ปิดเนื้อคลุมไส้ ไม่ใช่ Inside Bar'
      },
      {
        id: 'opt-scob-2',
        text: 'เกิด Bearish SCOB ที่สมบูรณ์แบบ ให้เปิด Sell โดยวาง Stop Loss ไว้เหนือปลายไส้แท่งที่ 1 (1.2755) เพียงเล็กน้อย',
        isCorrect: true,
        feedback: 'ยอดเยี่ยมที่สุด! หน้า 86-88 ระบุว่า SCOB ใช้ยืนยันหลังแตะ POI โดยแท่งแรก Sweep และแท่งที่สองปิดเนื้อคลุมไส้ ทำให้วาง SL ได้แคบมากและ R:R สูงมาก'
      },
      {
        id: 'opt-scob-3',
        text: 'เป็นสัญญาณ Buy เพราะแท่งที่ 1 ทำ Higher High สำเร็จ',
        isCorrect: false,
        feedback: 'ผิดทางอย่างสิ้นเชิง! ราคาอยู่ที่ Supply Zone และแท่งที่ 1 เป็นการ Sweep Liquidity ไม่ใช่การเบรคเพื่อไปต่อ'
      }
    ],
    institutionalExplanation: 'SCOB คืออาวุธลับของ SMC เพราะช่วยให้คุณยืนยันการกลับตัวในระดับแท่งเทียนโดยไม่ต้องรอโครงสร้างหลายชั่วโมง ทำให้ได้ Stop Loss ที่คมและ Risk:Reward สูงถึง 1:5 ถึง 1:10'
  },
  {
    id: 'sim-5-premium-discount-filter',
    title: 'สถานการณ์ที่ 5: การคัดกรองโซนด้วย Fibonacci Premium vs Discount',
    category: 'Fibonacci',
    difficulty: 'Intermediate',
    setupDescription: 'โครงสร้างสวิงหลักใน Timeframe H4 อยู่ในแนวโน้มขาขึ้น โดยมี Low อยู่ที่ 1.0500 และ High อยู่ที่ 1.0900 ระดับกึ่งกลาง 50% (Equilibrium) อยู่ที่ 1.0700 คุณพบ Order Block ฝั่ง Buy อยู่ 2 โซน: โซนที่ 1 อยู่ที่ 1.0780 และโซนที่ 2 อยู่ที่ 1.0620',
    chartRenderUrl: '/extracted/page_renders/page_111.png',
    originalPageRef: 111,
    question: 'ตามหลักการของ E-Book หน้า 109-111 คุณควรเลือกวางแผน Buy ที่โซนใด?',
    options: [
      {
        id: 'opt-fibo-1',
        text: 'โซนที่ 1 (1.0780) เพราะอยู่ใกล้ราคาปัจจุบันที่สุด จะได้ไม่ตกรถ',
        isCorrect: false,
        feedback: 'อันตราย! 1.0780 อยู่เหนือ 1.0700 ซึ่งจัดอยู่ใน Premium Zone (โซนของแพง) หน้า 110 ระบุว่าโซน Premium เหมาะสำหรับการขาย ไม่ใช่การซื้อ'
      },
      {
        id: 'opt-fibo-2',
        text: 'โซนที่ 2 (1.0620) เพราะอยู่ต่ำกว่าระดับ 50% ซึ่งจัดอยู่ใน Discount Zone (โซนของถูก) เหมาะแก่การ Buy',
        isCorrect: true,
        feedback: 'ถูกต้องสมบูรณ์แบบ! หน้า 111 ของ E-Book ระบุว่า ให้หา OB ในโซน discount หรือโซนของถูก ทำให้ได้เปรียบต้นทุนและสอดคล้องกับพฤติกรรม Smart Money'
      },
      {
        id: 'opt-fibo-3',
        text: 'เข้า Buy ทั้งสองโซนพร้อมกันแบบเบิ้ลไม้',
        isCorrect: false,
        feedback: 'ผิดหลักการ Money Management และฝืนกฎการคัดกรองด้วย Premium/Discount'
      }
    ],
    institutionalExplanation: 'Smart Money คือพ่อค้ารายใหญ่ พวกเขาจะรอให้ราคาลดกระหน่ำลงมาในเขต Discount Zone ก่อนที่จะเริ่มกวาดซื้อ การ Buy ในโซน Premium มีโอกาสสูงมากที่จะถูกทุบหลุดลงมาหา Discount Zone'
  },
  {
    id: 'sim-6-complete-model-entry',
    title: 'สถานการณ์ที่ 6: การบริหารหน้าไม้และปิดกำไรตามพิมพ์เขียว Model Entry',
    category: 'Full SMC Execution',
    difficulty: 'Advanced',
    setupDescription: 'คุณเปิด Buy ตาม Model Entry หน้า 113-115 ที่จุด Discount OB ราคา 2000 โดยมี Stop Loss ที่ 1994 (เสี่ยง 60 จุด) ปัจจุบันราคาวิ่งขึ้นไปถึง 2018 (กำไร 180 จุด หรือ R:R 1:3 แล้ว) และมีจุด Equal Highs (EQH / BSL) สำคัญของ Timeframe H4 อยู่ที่ราคา 2030',
    chartRenderUrl: '/extracted/page_renders/page_114.png',
    originalPageRef: 114,
    question: 'ตามระบบ SMC และหลักจิตวิทยาหน้า 112 คุณควรจัดการออเดอร์นี้อย่างไรให้เป็นมืออาชีพ?',
    options: [
      {
        id: 'opt-me-1',
        text: 'ปล่อยทิ้งไว้โดยไม่เลื่อน SL และถือยาวไปตลอดชีวิต',
        isCorrect: false,
        feedback: 'ขาดการบริหารความเสี่ยง ตลาดสามารถกลับตัวมากินทุนได้เสมอ'
      },
      {
        id: 'opt-me-2',
        text: 'เลื่อน Stop Loss มาบังหน้าทุน (Break-Even) หรือ Partial TP เก็บกำไรบางส่วน แล้วปล่อยส่วนที่เหลือวิ่งไป TP ที่จุด BSL (2030)',
        isCorrect: true,
        feedback: 'ถูกต้องแบบเซียน SMC! การเลื่อนกันทุนทำให้การเทรดนี้ Risk-Free (ไร้ความเสี่ยง) และการเล็ง TP ที่ BSL ด้านบนคือการใช้สภาพคล่องเป็นจุดออกตามธรรมชาติของตลาด'
      },
      {
        id: 'opt-me-3',
        text: 'ปิดทำกำไรทั้งหมดทันทีที่ได้ 10 จุด เพราะกลัวตลาดแย่งเงินคืน',
        isCorrect: false,
        feedback: 'การปิดเร็วเกินไปโดยไม่ปล่อยให้กำไรวิ่งตาม R:R จะทำให้ในระยะยาวพอร์ตไม่สามารถเติบโตชดเชยไม้ที่แพ้ได้'
      }
    ],
    institutionalExplanation: 'จุด BSL ที่ 2030 มีคำสั่ง Buy Stop ของรายย่อยรออยู่หนาแน่น เมื่อราคาพุ่งไปชนจุดนั้น สถาบันจะใช้สภาพคล่องตรงนั้นในการเทขายปิดกำไร การตั้ง TP ที่ BSL จึงเป็นจุดออกที่มีประสิทธิภาพสูงสุด'
  }
]
"""

with open(r"C:\Users\New JA\Downloads\EbookFOREX\src\data\curriculum.ts", "w", encoding="utf-8") as f:
    f.write(script_content)

print("Generated src/data/curriculum.ts successfully!")
