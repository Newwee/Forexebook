import React from 'react'
import {
  BookOpen,
  CheckCircle2,
  Flame,
  Award,
  ArrowRight,
  TrendingUp,
  Target,
  Sparkles,
  Layers,
  AlertTriangle,
  RotateCcw,
  Clock,
  Compass
} from 'lucide-react'
import { useProgress } from '../context/ProgressContext'
import { CHAPTERS } from '../data/curriculum'

interface DashboardProps {
  onStartLesson: (chapterId: string, lessonId: string) => void
  onTakeQuiz: (chapterId: string) => void
  onGoToTab: (tab: string) => void
}

export const Dashboard: React.FC<DashboardProps> = ({
  onStartLesson,
  onTakeQuiz,
  onGoToTab
}) => {
  const { progress } = useProgress()

  const totalLessons = CHAPTERS.reduce((acc, ch) => acc + ch.lessons.length, 0)
  const completedLessonsCount = progress.completedLessons.length
  const totalChapters = CHAPTERS.length
  const completedChaptersCount = progress.completedChapters.length
  const progressPercent = Math.round((completedLessonsCount / totalLessons) * 100) || 0

  const quizKeys = Object.keys(progress.quizScores)
  const totalQuizzesPassed = quizKeys.filter(k => progress.quizScores[k]?.passed).length
  const averageQuizScore = quizKeys.length > 0
    ? Math.round(
        (quizKeys.reduce((acc, k) => {
          const item = progress.quizScores[k]
          return acc + (item ? (item.score / item.total) * 100 : 0)
        }, 0) / quizKeys.length)
      )
    : 0

  let currentChapter = CHAPTERS[0]
  let currentLesson = CHAPTERS[0].lessons[0]

  if (progress.lastLessonId) {
    for (const ch of CHAPTERS) {
      const found = ch.lessons.find(l => l.id === progress.lastLessonId)
      if (found) {
        currentChapter = ch
        currentLesson = found
        break
      }
    }
  }

  let nextChapter = CHAPTERS[0]
  let nextLesson = CHAPTERS[0].lessons[0]
  let foundIncomplete = false

  for (const ch of CHAPTERS) {
    for (const l of ch.lessons) {
      if (!progress.completedLessons.includes(l.id)) {
        nextChapter = ch
        nextLesson = l
        foundIncomplete = true
        break
      }
    }
    if (foundIncomplete) break
  }

  const categories = [
    { id: 'Foundations', label: 'พื้นฐาน & Demand/Supply', color: 'from-blue-500 to-cyan-500' },
    { id: 'Structure', label: 'โครงสร้างตลาด & BOS', color: 'from-emerald-500 to-teal-500' },
    { id: 'Liquidity', label: 'สภาพคล่อง & IDM', color: 'from-amber-500 to-orange-500' },
    { id: 'Entry Execution', label: 'จุดเข้าเทรด OB/SCOB', color: 'from-indigo-500 to-purple-500' },
    { id: 'Mastery', label: 'จิตวิทยา & พิมพ์เขียว Model Entry', color: 'from-rose-500 to-pink-500' }
  ]

  return (
    <div className="space-y-6 sm:space-y-8 animate-in fade-in duration-300">
      <div className="relative overflow-hidden rounded-3xl glass-card border border-emerald-500/20 p-6 sm:p-8 lg:p-10 shadow-2xl">
        <div className="absolute top-0 right-0 -mt-16 -mr-16 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute bottom-0 left-1/3 -mb-20 w-72 h-72 bg-blue-500/10 rounded-full blur-3xl pointer-events-none" />

        <div className="relative z-10 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
          <div className="max-w-2xl space-y-3">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-semibold">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Smart Money Concepts (SMC) Masterclass</span>
            </div>
            <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-white tracking-tight leading-snug">
              เส้นทางสู่การเป็นเทรดเดอร์มืออาชีพกับ{' '}
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-300">
                SMC WARRIORS
              </span>
            </h1>
            <p className="text-sm sm:text-base text-slate-300 leading-relaxed">
              "จงปรับปรุงแล้วแก้ไข ยอมรับทุกความผิดพลาดเก็บเป็นประสบการณ์ อย่าเร่งรีบ แค่ชนะตัวเองได้ ก็ดีมากแล้ว" (หน้า 112)
            </p>
          </div>

          <div className="flex flex-col sm:flex-row lg:flex-col items-stretch sm:items-center lg:items-end gap-3 w-full lg:w-auto">
            <button
              onClick={() => onStartLesson(currentChapter.id, currentLesson.id)}
              className="flex items-center justify-center gap-2.5 px-6 py-3.5 rounded-2xl bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-400 hover:to-emerald-500 text-slate-950 font-bold text-sm sm:text-base shadow-lg shadow-emerald-500/25 transition-all hover:scale-[1.02] active:scale-[0.98] touch-target"
            >
              <span>เรียนต่อจากครั้งล่าสุด</span>
              <ArrowRight className="w-4 h-4 stroke-[2.5]" />
            </button>
            <button
              onClick={() => onGoToTab('simulator')}
              className="flex items-center justify-center gap-2 px-5 py-3 rounded-2xl bg-slate-800/80 hover:bg-slate-700/80 text-white font-semibold text-xs sm:text-sm border border-slate-700/60 transition-all touch-target"
            >
              <Target className="w-4 h-4 text-emerald-400" />
              <span>ฝึกจำลองสถานการณ์กราฟจริง</span>
            </button>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-5">
        <div className="glass-card p-4 sm:p-5 rounded-2xl border border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400 mb-3">
            <span className="text-xs sm:text-sm font-medium">ความคืบหน้ารวม</span>
            <div className="w-8 h-8 rounded-xl bg-emerald-500/10 text-emerald-400 flex items-center justify-center">
              <TrendingUp className="w-4 h-4" />
            </div>
          </div>
          <div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white mb-1">
              {progressPercent}%
            </div>
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mb-2">
              <div
                className="bg-gradient-to-r from-emerald-500 to-teal-400 h-full rounded-full transition-all duration-500"
                style={{ width: `${progressPercent}%` }}
              />
            </div>
            <p className="text-[11px] text-slate-400">
              สำเร็จแล้ว {completedLessonsCount} จาก {totalLessons} บทเรียน
            </p>
          </div>
        </div>

        <div className="glass-card p-4 sm:p-5 rounded-2xl border border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400 mb-3">
            <span className="text-xs sm:text-sm font-medium">บทที่ผ่านการประเมิน</span>
            <div className="w-8 h-8 rounded-xl bg-blue-500/10 text-blue-400 flex items-center justify-center">
              <BookOpen className="w-4 h-4" />
            </div>
          </div>
          <div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white mb-1">
              {completedChaptersCount} <span className="text-base text-slate-400 font-normal">/ {totalChapters}</span>
            </div>
            <p className="text-[11px] text-slate-400">
              ผ่านเกณฑ์ Quiz 80% ขึ้นไป
            </p>
          </div>
        </div>

        <div className="glass-card p-4 sm:p-5 rounded-2xl border border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400 mb-3">
            <span className="text-xs sm:text-sm font-medium">สถิติความต่อเนื่อง</span>
            <div className="w-8 h-8 rounded-xl bg-amber-500/10 text-amber-400 flex items-center justify-center">
              <Flame className="w-4 h-4 fill-amber-400/30" />
            </div>
          </div>
          <div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white mb-1">
              {progress.streak} <span className="text-base text-slate-400 font-normal">วัน</span>
            </div>
            <p className="text-[11px] text-slate-400">
              เรียนต่อเนื่องเพื่อสร้างวินัย
            </p>
          </div>
        </div>

        <div className="glass-card p-4 sm:p-5 rounded-2xl border border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400 mb-3">
            <span className="text-xs sm:text-sm font-medium">คะแนนแบบทดสอบ</span>
            <div className="w-8 h-8 rounded-xl bg-purple-500/10 text-purple-400 flex items-center justify-center">
              <Award className="w-4 h-4" />
            </div>
          </div>
          <div>
            <div className="text-2xl sm:text-3xl font-extrabold text-white mb-1">
              {averageQuizScore}%
            </div>
            <p className="text-[11px] text-slate-400">
              เฉลี่ยจาก {quizKeys.length} บททดสอบ
            </p>
          </div>
        </div>
      </div>

      {progress.weakTopics.length > 0 && (
        <div className="glass-card p-5 sm:p-6 rounded-2xl border border-amber-500/30 bg-amber-500/5">
          <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div className="flex items-start gap-3">
              <div className="p-2.5 rounded-xl bg-amber-500/20 text-amber-400 shrink-0">
                <AlertTriangle className="w-5 h-5" />
              </div>
              <div>
                <h3 className="text-base font-bold text-white mb-1">
                  หัวข้อที่ควรทบทวนเพิ่มเติม (คะแนนไม่ถึง 80%)
                </h3>
                <p className="text-xs sm:text-sm text-slate-300">
                  ระบบตรวจพบว่าคุณมีจุดที่ยังไม่เข้าใจในหัวข้อ: {progress.weakTopics.join(', ')}
                </p>
              </div>
            </div>
            <button
              onClick={() => onGoToTab('mistakes')}
              className="px-4 py-2 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 font-semibold text-xs sm:text-sm border border-amber-500/40 transition-colors whitespace-nowrap touch-target flex items-center gap-2"
            >
              <RotateCcw className="w-4 h-4" />
              <span>ดูข้อที่ตอบผิดและเฉลย</span>
            </button>
          </div>
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-6">
          <div className="glass-card p-5 sm:p-6 rounded-2xl border border-slate-800">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2.5">
                <Layers className="w-5 h-5 text-emerald-400" />
                <h2 className="text-lg font-bold text-white">ความก้าวหน้าตามหมวดหมู่เนื้อหา</h2>
              </div>
              <button
                onClick={() => onGoToTab('curriculum')}
                className="text-xs font-semibold text-emerald-400 hover:text-emerald-300 flex items-center gap-1"
              >
                <span>ดูทั้งหมด</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>

            <div className="space-y-4">
              {categories.map(cat => {
                const catChapters = CHAPTERS.filter(c => c.category === cat.id)
                const catLessonIds = catChapters.flatMap(c => c.lessons.map(l => l.id))
                const catCompleted = catLessonIds.filter(id => progress.completedLessons.includes(id)).length
                const percent = Math.round((catCompleted / (catLessonIds.length || 1)) * 100)

                return (
                  <div key={cat.id} className="space-y-1.5">
                    <div className="flex items-center justify-between text-xs sm:text-sm">
                      <span className="font-medium text-slate-300">{cat.label}</span>
                      <span className="font-semibold text-slate-400">
                        {catCompleted}/{catLessonIds.length} ({percent}%)
                      </span>
                    </div>
                    <div className="w-full bg-slate-800/80 h-2 rounded-full overflow-hidden">
                      <div
                        className={`h-full rounded-full bg-gradient-to-r ${cat.color} transition-all duration-500`}
                        style={{ width: `${percent}%` }}
                      />
                    </div>
                  </div>
                )
              })}
            </div>
          </div>

          <div className="glass-card p-5 sm:p-6 rounded-2xl border border-slate-800">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2.5">
                <BookOpen className="w-5 h-5 text-emerald-400" />
                <h2 className="text-lg font-bold text-white">บทเรียนแนะนำถัดไป</h2>
              </div>
              <span className="text-xs px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-400 font-semibold border border-emerald-500/20">
                Next Step
              </span>
            </div>

            <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800/80 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div className="space-y-1">
                <div className="flex items-center gap-2 text-xs text-slate-400">
                  <span className="font-bold text-emerald-400">บทที่ {nextChapter.chapterNumber}</span>
                  <span>•</span>
                  <span>หน้า {nextChapter.pdfPages}</span>
                  <span>•</span>
                  <span className="flex items-center gap-1">
                    <Clock className="w-3 h-3" /> {nextChapter.estimatedMinutes} นาที
                  </span>
                </div>
                <h3 className="text-base font-bold text-white">
                  {nextLesson.title}
                </h3>
                <p className="text-xs text-slate-400 line-clamp-1">
                  {nextChapter.shortDescription}
                </p>
              </div>
              <button
                onClick={() => onStartLesson(nextChapter.id, nextLesson.id)}
                className="px-5 py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs sm:text-sm whitespace-nowrap shadow-md shadow-emerald-500/20 transition-all touch-target"
              >
                เริ่มเรียนตอนนี้
              </button>
            </div>
          </div>
        </div>

        <div className="space-y-6">
          <div className="glass-card p-5 sm:p-6 rounded-2xl border border-slate-800">
            <h2 className="text-lg font-bold text-white mb-3">คลังคำศัพท์ไฮไลต์</h2>
            <p className="text-xs text-slate-400 mb-4">
              คำศัพท์ SMC สถาบันที่พบบ่อยใน E-Book Trade.pdf
            </p>
            <div className="space-y-2.5">
              {[
                { term: 'Valid Pullback', meaning: 'การพักราคาที่กวาด Low/High แท่งสูงสุด/ต่ำสุด' },
                { term: 'IDM (Inducement)', meaning: 'กับดักล่อซื้อขาย คอนเฟิร์ม High/Low แท้จริง' },
                { term: 'BOS (Break of Structure)', meaning: 'การเบรคด้วยเนื้อเทียนเพื่อไปต่อตามเทรน' },
                { term: 'SCOB', meaning: 'Single Candle OB คอนเฟิร์มหลังแตะ POI' },
                { term: 'Order Flow (OF)', meaning: 'แรงส่งสุดท้าย กฎเหล็กใช้ได้เพียง 1 ครั้ง' }
              ].map((item, idx) => (
                <div
                  key={idx}
                  onClick={() => onGoToTab('glossary')}
                  className="p-3 rounded-xl bg-slate-900/60 hover:bg-slate-800/80 border border-slate-800/60 cursor-pointer transition-colors"
                >
                  <div className="font-bold text-xs sm:text-sm text-emerald-400 mb-0.5">
                    {item.term}
                  </div>
                  <div className="text-[11px] sm:text-xs text-slate-300">
                    {item.meaning}
                  </div>
                </div>
              ))}
            </div>
            <button
              onClick={() => onGoToTab('glossary')}
              className="w-full mt-4 py-2.5 rounded-xl bg-slate-800/60 hover:bg-slate-800 text-slate-300 hover:text-white font-medium text-xs border border-slate-700/50 transition-colors touch-target"
            >
              เปิดคลังคำศัพท์ทั้งหมด 25+ คำ
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
