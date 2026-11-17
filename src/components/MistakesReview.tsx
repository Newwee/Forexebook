import React from 'react'
import {
  AlertTriangle,
  CheckCircle2,
  XCircle,
  BookOpen,
  RotateCcw,
  Sparkles,
  ArrowRight,
  ShieldCheck
} from 'lucide-react'
import { useProgress } from '../context/ProgressContext'
import { CHAPTERS } from '../data/curriculum'

interface MistakesReviewProps {
  onGoToLesson: (chapterId: string) => void
  onRetakeQuiz: (chapterId: string) => void
}

export const MistakesReview: React.FC<MistakesReviewProps> = ({
  onGoToLesson,
  onRetakeQuiz
}) => {
  const { progress } = useProgress()
  const incorrectKeys = Object.keys(progress.incorrectQuestions)

  if (incorrectKeys.length === 0) {
    return (
      <div className="max-w-2xl mx-auto py-12 px-4 text-center space-y-6 animate-in fade-in duration-300">
        <div className="w-20 h-20 mx-auto rounded-3xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-center shadow-xl">
          <ShieldCheck className="w-10 h-10" />
        </div>
        <div className="space-y-2">
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
            ยอดเยี่ยมมาก! ยังไม่มีข้อที่ตอบผิดสะสม
          </h2>
          <p className="text-xs sm:text-sm text-slate-400 max-w-md mx-auto leading-relaxed">
            คุณยังไม่มีประวัติข้อที่ตอบผิด หรือผ่านการประเมินทุกบทเรียนแล้วอย่างราบรื่น
          </p>
        </div>
        <button
          onClick={() => onRetakeQuiz(CHAPTERS[0].id)}
          className="px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 text-slate-950 font-bold text-xs sm:text-sm shadow-md shadow-emerald-500/20 touch-target"
        >
          ทำแบบทดสอบเพื่อทดสอบความรู้
        </button>
      </div>
    )
  }

  return (
    <div className="space-y-6 sm:space-y-8 animate-in fade-in duration-300">
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/20 text-amber-400 text-xs font-semibold mb-2">
            <AlertTriangle className="w-3.5 h-3.5" />
            <span>Weak Topics & Error Analysis</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            ทบทวนข้อที่ตอบผิด & วิเคราะห์จุดอ่อน ({incorrectKeys.length} ข้อ)
          </h1>
          <p className="text-xs sm:text-sm text-slate-400 mt-1">
            "ยอมรับทุกความผิดพลาดเก็บเป็นประสบการณ์ ทุกความผิดพลาดสอนให้เราอย่าทำพลาดอีก" (หน้า 112)
          </p>
        </div>
      </div>

      {progress.weakTopics.length > 0 && (
        <div className="p-4 sm:p-5 rounded-2xl bg-amber-500/10 border border-amber-500/30 flex items-center gap-3">
          <AlertTriangle className="w-5 h-5 text-amber-400 shrink-0" />
          <div className="text-xs sm:text-sm text-slate-200">
            <span className="font-bold text-amber-400">หัวข้อที่ยังไม่ผ่านเกณฑ์ 80%:</span>{' '}
            {progress.weakTopics.join(', ')}
          </div>
        </div>
      )}

      <div className="space-y-4">
        {incorrectKeys.map(key => {
          const item = progress.incorrectQuestions[key]
          let relatedChapter = CHAPTERS[0]

          for (const ch of CHAPTERS) {
            if (ch.quiz.some(q => q.id === key)) {
              relatedChapter = ch
              break
            }
          }

          return (
            <div
              key={key}
              className="glass-card rounded-2xl border border-slate-800 p-5 sm:p-6 space-y-4 hover:border-slate-700 transition-colors"
            >
              <div className="flex items-center justify-between gap-2">
                <span className="text-xs font-bold text-emerald-400">
                  บทที่ {relatedChapter.chapterNumber}: {relatedChapter.title}
                </span>
                <button
                  onClick={() => onRetakeQuiz(relatedChapter.id)}
                  className="text-xs text-amber-400 hover:text-amber-300 font-semibold flex items-center gap-1 touch-target"
                >
                  <RotateCcw className="w-3.5 h-3.5" />
                  <span>ทำแบบทดสอบบทนี้ใหม่</span>
                </button>
              </div>

              <h3 className="text-sm sm:text-base font-bold text-white leading-relaxed">
                {item.question}
              </h3>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div className="p-3.5 rounded-xl bg-rose-950/20 border border-rose-500/30 space-y-1">
                  <div className="flex items-center gap-1.5 text-xs font-bold text-rose-400">
                    <XCircle className="w-4 h-4" />
                    <span>คำตอบที่คุณเลือก (ไม่ถูกต้อง)</span>
                  </div>
                  <p className="text-xs text-slate-300">
                    {item.yourAnswer}
                  </p>
                </div>

                <div className="p-3.5 rounded-xl bg-emerald-950/20 border border-emerald-500/30 space-y-1">
                  <div className="flex items-center gap-1.5 text-xs font-bold text-emerald-400">
                    <CheckCircle2 className="w-4 h-4" />
                    <span>คำตอบที่ถูกต้องตามหลัก SMC</span>
                  </div>
                  <p className="text-xs text-emerald-300 font-medium">
                    {item.correctAnswer}
                  </p>
                </div>
              </div>

              <div className="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1.5">
                <div className="flex items-center gap-2 text-xs font-bold text-amber-400">
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>เหตุผลและหลักการที่ถูกต้อง</span>
                </div>
                <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                  {item.explanation}
                </p>
              </div>

              <div className="pt-2 flex justify-end">
                <button
                  onClick={() => onGoToLesson(relatedChapter.id)}
                  className="flex items-center gap-1.5 text-xs font-semibold text-emerald-400 hover:text-emerald-300"
                >
                  <BookOpen className="w-3.5 h-3.5" />
                  <span>อ่านทบทวนบทเรียนที่เกี่ยวข้อง</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
