import React, { useState } from 'react'
import {
  Award,
  CheckCircle2,
  XCircle,
  HelpCircle,
  ArrowRight,
  RotateCcw,
  BookOpen,
  Sparkles,
  AlertTriangle,
  ArrowLeft
} from 'lucide-react'
import { CHAPTERS } from '../data/curriculum'
import { useProgress } from '../context/ProgressContext'
import { IncorrectQuestionRecord } from '../types'

interface QuizViewProps {
  chapterId: string
  onClose: () => void
  onReviewChapter: (chapterId: string) => void
  onNextChapter: (chapterId: string) => void
}

export const QuizView: React.FC<QuizViewProps> = ({
  chapterId,
  onClose,
  onReviewChapter,
  onNextChapter
}) => {
  const { progress, saveQuizScore } = useProgress()
  const chapter = CHAPTERS.find(c => c.id === chapterId) || CHAPTERS[0]
  const questions = chapter.quiz

  const [currentIndex, setCurrentIndex] = useState(0)
  const [selectedOption, setSelectedOption] = useState<number | null>(null)
  const [isAnswerSubmitted, setIsAnswerSubmitted] = useState(false)
  const [userAnswers, setUserAnswers] = useState<Record<number, number>>({})
  const [isCompleted, setIsCompleted] = useState(false)

  const currentQ = questions[currentIndex]

  const handleSelectOption = (index: number) => {
    if (isAnswerSubmitted) return
    setSelectedOption(index)
  }

  const handleSubmitAnswer = () => {
    if (selectedOption === null) return
    setIsAnswerSubmitted(true)
    setUserAnswers(prev => ({ ...prev, [currentIndex]: selectedOption }))
  }

  const handleNextQuestion = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(prev => prev + 1)
      setSelectedOption(null)
      setIsAnswerSubmitted(false)
    } else {
      let correctCount = 0
      const incorrectRecords: Record<string, IncorrectQuestionRecord> = {}

      questions.forEach((q, idx) => {
        const ans = userAnswers[idx] !== undefined ? userAnswers[idx] : selectedOption
        if (ans === q.correctIndex) {
          correctCount++
        } else {
          incorrectRecords[q.id] = {
            question: q.question,
            yourAnswer: q.options[ans ?? 0] || 'ไม่ได้ตอบ',
            correctAnswer: q.options[q.correctIndex],
            explanation: q.explanation
          }
        }
      })

      saveQuizScore(chapter.id, correctCount, questions.length, incorrectRecords, chapter.title)
      setIsCompleted(true)
    }
  }

  const handleRestartQuiz = () => {
    setCurrentIndex(0)
    setSelectedOption(null)
    setIsAnswerSubmitted(false)
    setUserAnswers({})
    setIsCompleted(false)
  }

  const calculateFinalScore = () => {
    let correct = 0
    questions.forEach((q, idx) => {
      if (userAnswers[idx] === q.correctIndex) {
        correct++
      }
    })
    return correct
  }

  const score = calculateFinalScore()
  const percentage = Math.round((score / questions.length) * 100)
  const isPassed = percentage >= 80

  const nextChapterIndex = CHAPTERS.findIndex(c => c.id === chapter.id) + 1
  const hasNextChapter = nextChapterIndex < CHAPTERS.length

  if (isCompleted) {
    return (
      <div className="max-w-2xl mx-auto space-y-6 p-4 sm:p-6 animate-in zoom-in-95 duration-300">
        <div className={`glass-card p-6 sm:p-8 rounded-3xl border text-center space-y-5 ${
          isPassed
            ? 'border-emerald-500/40 bg-emerald-950/10'
            : 'border-amber-500/40 bg-amber-950/10'
        }`}>
          <div className="w-16 h-16 sm:w-20 sm:h-20 mx-auto rounded-3xl bg-slate-900 border border-slate-700/80 flex items-center justify-center shadow-xl">
            {isPassed ? (
              <Award className="w-8 h-8 sm:w-10 sm:h-10 text-emerald-400" />
            ) : (
              <AlertTriangle className="w-8 h-8 sm:w-10 sm:h-10 text-amber-400" />
            )}
          </div>

          <div className="space-y-2">
            <span className={`text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full ${
              isPassed
                ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
                : 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
            }`}>
              {isPassed ? 'ผ่านเกณฑ์ประเมิน (Passed)' : 'ต้องทบทวนเนื้อหา (Needs Review)'}
            </span>
            <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
              {isPassed ? 'ยินดีด้วย! คุณเข้าใจเนื้อหาอย่างลึกซึ้ง' : 'อย่าเพิ่งท้อ! ยอมรับข้อผิดพลาดแล้วพัฒนา'}
            </h2>
            <p className="text-xs sm:text-sm text-slate-300 max-w-md mx-auto">
              {isPassed
                ? `คุณทำคะแนนได้ยอดเยี่ยมและพร้อมก้าวสู่บทถัดไปของ SMC Warriors แล้ว`
                : `เกณฑ์ผ่านคือ 80% (คุณได้ ${percentage}%) แนะนำให้กลับไปทบทวนเนื้อหาก่อนทำแบบทดสอบใหม่อีกครั้ง`}
            </p>
          </div>

          <div className="p-4 rounded-2xl bg-slate-900/80 border border-slate-800 max-w-sm mx-auto flex items-center justify-around">
            <div>
              <div className="text-xs text-slate-400 mb-1">คะแนนที่ได้</div>
              <div className="text-2xl font-black text-white">
                {score} <span className="text-sm font-normal text-slate-400">/ {questions.length}</span>
              </div>
            </div>
            <div className="h-8 w-px bg-slate-800" />
            <div>
              <div className="text-xs text-slate-400 mb-1">คิดเป็น</div>
              <div className={`text-2xl font-black ${isPassed ? 'text-emerald-400' : 'text-amber-400'}`}>
                {percentage}%
              </div>
            </div>
          </div>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-3">
            <button
              onClick={handleRestartQuiz}
              className="w-full sm:w-auto px-5 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-semibold text-xs sm:text-sm border border-slate-700/60 flex items-center justify-center gap-2 touch-target"
            >
              <RotateCcw className="w-4 h-4" />
              <span>ทำแบบทดสอบอีกครั้ง</span>
            </button>

            <button
              onClick={() => onReviewChapter(chapter.id)}
              className="w-full sm:w-auto px-5 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs sm:text-sm border border-slate-700/60 flex items-center justify-center gap-2 touch-target"
            >
              <BookOpen className="w-4 h-4 text-emerald-400" />
              <span>ทบทวนเนื้อหาบทนี้</span>
            </button>

            {isPassed && hasNextChapter && (
              <button
                onClick={() => onNextChapter(CHAPTERS[nextChapterIndex].id)}
                className="w-full sm:w-auto px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-400 hover:to-emerald-500 text-slate-950 font-bold text-xs sm:text-sm shadow-lg shadow-emerald-500/25 flex items-center justify-center gap-2 touch-target"
              >
                <span>ไปบทถัดไป (บทที่ {CHAPTERS[nextChapterIndex].chapterNumber})</span>
                <ArrowRight className="w-4 h-4 stroke-[2.5]" />
              </button>
            )}
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-3xl mx-auto space-y-6 p-4 sm:p-6 animate-in fade-in duration-300">
      <div className="flex items-center justify-between gap-3 pb-3 border-b border-slate-800">
        <button
          onClick={onClose}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-900 text-slate-400 hover:text-white border border-slate-800 text-xs font-semibold touch-target"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>ออกจากการทดสอบ</span>
        </button>

        <div className="flex items-center gap-2">
          <span className="text-xs font-medium text-slate-400">
            คำถามข้อที่ {currentIndex + 1} จาก {questions.length}
          </span>
          <div className="w-24 bg-slate-800 h-2 rounded-full overflow-hidden">
            <div
              className="bg-emerald-500 h-full transition-all duration-300"
              style={{ width: `${((currentIndex + 1) / questions.length) * 100}%` }}
            />
          </div>
        </div>
      </div>

      <div className="glass-card p-6 sm:p-8 rounded-3xl border border-slate-800 space-y-6">
        <div className="space-y-2">
          <div className="flex items-center gap-2">
            <span className="text-[11px] font-bold px-2 py-0.5 rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              {currentQ.type === 'mcq'
                ? 'คำถามปรนัย'
                : currentQ.type === 'scenario'
                ? 'จำลองสถานการณ์จริง'
                : currentQ.type === 'chart'
                ? 'วิเคราะห์กราฟ'
                : 'ถูกหรือผิด (True/False)'}
            </span>
            <span className="text-xs text-slate-400 font-mono">
              บทที่ {chapter.chapterNumber}: {chapter.title}
            </span>
          </div>

          <h2 className="text-base sm:text-xl font-bold text-white leading-relaxed">
            {currentQ.question}
          </h2>
        </div>

        <div className="space-y-3">
          {currentQ.options.map((option, idx) => {
            const isSelected = selectedOption === idx
            const isCorrect = idx === currentQ.correctIndex

            let optionStyle = 'bg-slate-900/80 border-slate-800 text-slate-200 hover:bg-slate-800 hover:border-slate-700'

            if (isAnswerSubmitted) {
              if (isCorrect) {
                optionStyle = 'bg-emerald-950/40 border-emerald-500 text-emerald-200 shadow-md shadow-emerald-500/10'
              } else if (isSelected && !isCorrect) {
                optionStyle = 'bg-rose-950/40 border-rose-500 text-rose-200'
              } else {
                optionStyle = 'bg-slate-900/40 border-slate-800/60 text-slate-500 opacity-60'
              }
            } else if (isSelected) {
              optionStyle = 'bg-emerald-500/15 border-emerald-500 text-emerald-300 ring-1 ring-emerald-500'
            }

            return (
              <button
                key={idx}
                disabled={isAnswerSubmitted}
                onClick={() => handleSelectOption(idx)}
                className={`w-full text-left p-4 rounded-2xl border transition-all flex items-start gap-3 touch-target ${optionStyle}`}
              >
                <span className={`w-6 h-6 rounded-lg flex items-center justify-center shrink-0 text-xs font-bold ${
                  isAnswerSubmitted && isCorrect
                    ? 'bg-emerald-500 text-slate-950'
                    : isAnswerSubmitted && isSelected && !isCorrect
                    ? 'bg-rose-500 text-white'
                    : isSelected
                    ? 'bg-emerald-500 text-slate-950'
                    : 'bg-slate-800 text-slate-400'
                }`}>
                  {String.fromCharCode(65 + idx)}
                </span>
                <span className="text-xs sm:text-sm font-medium leading-relaxed pt-0.5">
                  {option}
                </span>
              </button>
            )
          })}
        </div>

        {isAnswerSubmitted && (
          <div className={`p-5 rounded-2xl border space-y-2.5 animate-in slide-in-from-bottom-2 duration-300 ${
            selectedOption === currentQ.correctIndex
              ? 'bg-emerald-950/30 border-emerald-500/40'
              : 'bg-rose-950/30 border-rose-500/40'
          }`}>
            <div className="flex items-center gap-2">
              {selectedOption === currentQ.correctIndex ? (
                <>
                  <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                  <span className="font-bold text-sm text-emerald-400">ยอดเยี่ยม! คำตอบถูกต้อง</span>
                </>
              ) : (
                <>
                  <XCircle className="w-5 h-5 text-rose-400" />
                  <span className="font-bold text-sm text-rose-400">ยังไม่ถูกต้อง</span>
                </>
              )}
            </div>

            <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
              {currentQ.explanation}
            </p>

            <div className="pt-2 text-[11px] text-slate-400 font-mono flex items-center gap-1.5">
              <BookOpen className="w-3.5 h-3.5 text-emerald-400" />
              <span>แหล่งอ้างอิง: {currentQ.referenceConcept}</span>
            </div>
          </div>
        )}

        <div className="pt-4 border-t border-slate-800 flex items-center justify-end">
          {!isAnswerSubmitted ? (
            <button
              disabled={selectedOption === null}
              onClick={handleSubmitAnswer}
              className={`px-6 py-3 rounded-xl font-bold text-xs sm:text-sm transition-all touch-target ${
                selectedOption !== null
                  ? 'bg-emerald-500 hover:bg-emerald-400 text-slate-950 shadow-md shadow-emerald-500/20'
                  : 'bg-slate-800 text-slate-500 cursor-not-allowed'
              }`}
            >
              ตรวจคำตอบ
            </button>
          ) : (
            <button
              onClick={handleNextQuestion}
              className="flex items-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-400 text-slate-950 font-bold text-xs sm:text-sm shadow-md shadow-emerald-500/20 touch-target"
            >
              <span>{currentIndex < questions.length - 1 ? 'ข้อถัดไป' : 'ดูผลคะแนนการประเมิน'}</span>
              <ArrowRight className="w-4 h-4 stroke-[2.5]" />
            </button>
          )}
        </div>
      </div>
    </div>
  )
}
