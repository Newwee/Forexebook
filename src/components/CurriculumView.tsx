import React, { useState } from 'react'
import {
  BookOpen,
  CheckCircle2,
  Clock,
  Award,
  ArrowRight,
  Filter,
  Check,
  AlertCircle,
  Sparkles,
  Search
} from 'lucide-react'
import { CHAPTERS } from '../data/curriculum'
import { useProgress } from '../context/ProgressContext'
import { Category, Difficulty } from '../types'

interface CurriculumViewProps {
  onSelectLesson: (chapterId: string, lessonId: string) => void
  onTakeQuiz: (chapterId: string) => void
}

export const CurriculumView: React.FC<CurriculumViewProps> = ({
  onSelectLesson,
  onTakeQuiz
}) => {
  const { progress } = useProgress()
  const [selectedCategory, setSelectedCategory] = useState<string>('All')
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('All')
  const [searchQuery, setSearchQuery] = useState<string>('')

  const categories = [
    { id: 'All', label: 'ทั้งหมด (16 บท)' },
    { id: 'Foundations', label: 'พื้นฐาน & Demand/Supply' },
    { id: 'Structure', label: 'โครงสร้าง & BOS/CHoCH' },
    { id: 'Liquidity', label: 'สภาพคล่อง & IDM' },
    { id: 'Entry Execution', label: 'จุดเข้าเทรด OB/SCOB/BRK' },
    { id: 'Mastery', label: 'จิตวิทยา & Model Entry' }
  ]

  const filteredChapters = CHAPTERS.filter(ch => {
    if (selectedCategory !== 'All' && ch.category !== selectedCategory) return false
    if (selectedDifficulty !== 'All' && ch.difficulty !== selectedDifficulty) return false
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase()
      const matchTitle = ch.title.toLowerCase().includes(q)
      const matchEn = ch.englishTitle.toLowerCase().includes(q)
      const matchDesc = ch.shortDescription.toLowerCase().includes(q)
      const matchTerms = ch.keyTerms.some(t => t.term.toLowerCase().includes(q) || t.meaning.toLowerCase().includes(q))
      if (!matchTitle && !matchEn && !matchDesc && !matchTerms) return false
    }
    return true
  })

  return (
    <div className="space-y-6 sm:space-y-8 animate-in fade-in duration-300">
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-semibold mb-2">
            <BookOpen className="w-3.5 h-3.5" />
            <span>หลักสูตรฉบับสมบูรณ์ 116 หน้า</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            หลักสูตร SMC Warriors Trader E-Book
          </h1>
          <p className="text-xs sm:text-sm text-slate-400 mt-1">
            เรียบเรียงและถอดรหัสจาก Trade.pdf ครบถ้วนทุกกฎ ทุกเงื่อนไข และภาพกราฟจริง
          </p>
        </div>

        <div className="relative w-full md:w-72">
          <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            placeholder="ค้นหาบทเรียน เช่น IDM, BOS, SCOB..."
            className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-900/80 border border-slate-700/80 text-white placeholder-slate-500 text-xs sm:text-sm focus:outline-none focus:border-emerald-500 transition-colors"
          />
        </div>
      </div>

      <div className="flex flex-col sm:flex-row gap-3 items-start sm:items-center justify-between overflow-x-auto pb-1">
        <div className="flex items-center gap-1.5 flex-wrap">
          {categories.map(cat => (
            <button
              key={cat.id}
              onClick={() => setSelectedCategory(cat.id)}
              className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition-all touch-target ${
                selectedCategory === cat.id
                  ? 'bg-emerald-500 text-slate-950 shadow-md shadow-emerald-500/20'
                  : 'bg-slate-900/60 text-slate-300 hover:bg-slate-800 border border-slate-800'
              }`}
            >
              {cat.label}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-1.5 self-end sm:self-auto">
          {['All', 'Beginner', 'Intermediate', 'Advanced'].map(diff => (
            <button
              key={diff}
              onClick={() => setSelectedDifficulty(diff)}
              className={`px-2.5 py-1 rounded-lg text-[11px] font-semibold transition-all ${
                selectedDifficulty === diff
                  ? 'bg-slate-700 text-white'
                  : 'bg-slate-900/40 text-slate-400 hover:text-slate-200'
              }`}
            >
              {diff === 'All' ? 'ทุกระดับ' : diff}
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6">
        {filteredChapters.map(chapter => {
          const totalInChapter = chapter.lessons.length
          const completedInChapter = chapter.lessons.filter(l =>
            progress.completedLessons.includes(l.id)
          ).length
          const isFullyRead = completedInChapter === totalInChapter
          const quizRecord = progress.quizScores[chapter.id]
          const isPassed = quizRecord?.passed

          return (
            <div
              key={chapter.id}
              className={`glass-card rounded-2xl border transition-all duration-300 flex flex-col justify-between p-5 sm:p-6 ${
                isPassed
                  ? 'border-emerald-500/30 hover:border-emerald-500/50'
                  : 'border-slate-800 hover:border-slate-700'
              }`}
            >
              <div className="space-y-3 sm:space-y-4">
                <div className="flex items-center justify-between gap-2">
                  <div className="flex items-center gap-2">
                    <span className="w-7 h-7 rounded-lg bg-emerald-500/10 text-emerald-400 font-extrabold text-xs flex items-center justify-center border border-emerald-500/20">
                      {chapter.chapterNumber}
                    </span>
                    <span className="text-[11px] font-medium text-slate-400">
                      หน้า {chapter.pdfPages}
                    </span>
                  </div>

                  <div className="flex items-center gap-1.5">
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full uppercase tracking-wider ${
                      chapter.difficulty === 'Beginner'
                        ? 'bg-blue-500/10 text-blue-400 border border-blue-500/20'
                        : chapter.difficulty === 'Intermediate'
                        ? 'bg-amber-500/10 text-amber-400 border border-amber-500/20'
                        : 'bg-purple-500/10 text-purple-400 border border-purple-500/20'
                    }`}>
                      {chapter.difficulty}
                    </span>
                    <span className="text-[11px] text-slate-400 flex items-center gap-1">
                      <Clock className="w-3 h-3" /> {chapter.estimatedMinutes} นาที
                    </span>
                  </div>
                </div>

                <div>
                  <h3 className="text-base sm:text-lg font-bold text-white tracking-tight mb-1">
                    {chapter.title}
                  </h3>
                  <p className="text-xs font-mono text-emerald-400/90 mb-2">
                    {chapter.englishTitle}
                  </p>
                  <p className="text-xs sm:text-sm text-slate-300 line-clamp-2 leading-relaxed">
                    {chapter.shortDescription}
                  </p>
                </div>

                <div className="flex flex-wrap gap-1.5 pt-1">
                  {chapter.keyTerms.slice(0, 3).map((term, i) => (
                    <span
                      key={i}
                      className="text-[10px] sm:text-[11px] px-2 py-0.5 rounded-md bg-slate-800/80 text-slate-300 border border-slate-700/50"
                    >
                      {term.term}
                    </span>
                  ))}
                  {chapter.keyTerms.length > 3 && (
                    <span className="text-[10px] px-1.5 py-0.5 text-slate-400">
                      +{chapter.keyTerms.length - 3}
                    </span>
                  )}
                </div>
              </div>

              <div className="pt-5 mt-4 border-t border-slate-800/80 space-y-3">
                <div className="flex items-center justify-between text-xs text-slate-400">
                  <span className="flex items-center gap-1">
                    {isFullyRead ? (
                      <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                    ) : (
                      <BookOpen className="w-3.5 h-3.5 text-slate-400" />
                    )}
                    <span>บทเรียน: {completedInChapter}/{totalInChapter}</span>
                  </span>

                  {quizRecord && (
                    <span className={`font-semibold flex items-center gap-1 ${
                      isPassed ? 'text-emerald-400' : 'text-amber-400'
                    }`}>
                      <Award className="w-3.5 h-3.5" />
                      <span>Quiz: {quizRecord.score}/{quizRecord.total} ({isPassed ? 'ผ่าน' : 'ไม่ผ่าน'})</span>
                    </span>
                  )}
                </div>

                <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
                  <div
                    className="bg-emerald-500 h-full rounded-full transition-all duration-300"
                    style={{ width: `${(completedInChapter / totalInChapter) * 100}%` }}
                  />
                </div>

                <div className="flex items-center gap-2 pt-1">
                  <button
                    onClick={() => onSelectLesson(chapter.id, chapter.lessons[0].id)}
                    className="flex-1 flex items-center justify-center gap-1.5 py-2.5 rounded-xl bg-slate-800 hover:bg-emerald-500 hover:text-slate-950 text-white font-semibold text-xs transition-all touch-target border border-slate-700/60 hover:border-emerald-500"
                  >
                    <span>{isFullyRead ? 'อ่านทบทวน' : 'เข้าสู่บทเรียน'}</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>

                  <button
                    onClick={() => onTakeQuiz(chapter.id)}
                    className={`px-4 py-2.5 rounded-xl font-semibold text-xs transition-all touch-target flex items-center gap-1.5 ${
                      isPassed
                        ? 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30 hover:bg-emerald-500/25'
                        : 'bg-slate-800/80 text-slate-300 border border-slate-700/60 hover:bg-slate-700'
                    }`}
                  >
                    <Award className="w-3.5 h-3.5" />
                    <span>แบบทดสอบ</span>
                  </button>
                </div>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
