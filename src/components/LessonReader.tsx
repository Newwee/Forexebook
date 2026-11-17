import React, { useState, useEffect } from 'react'
import {
  ChevronLeft,
  ChevronRight,
  BookOpen,
  CheckCircle2,
  Bookmark,
  Share2,
  Clock,
  Sparkles,
  Award,
  Layers,
  ZoomIn,
  X,
  FileText,
  AlertTriangle,
  Lightbulb,
  ShieldAlert,
  ArrowLeft
} from 'lucide-react'
import { CHAPTERS } from '../data/curriculum'
import { useProgress } from '../context/ProgressContext'
import { Chapter, Lesson, OriginalImage } from '../types'

interface LessonReaderProps {
  chapterId: string
  lessonId: string
  onNavigateLesson: (chapterId: string, lessonId: string) => void
  onTakeQuiz: (chapterId: string) => void
  onBackToCurriculum: () => void
}

export const LessonReader: React.FC<LessonReaderProps> = ({
  chapterId,
  lessonId,
  onNavigateLesson,
  onTakeQuiz,
  onBackToCurriculum
}) => {
  const { progress, markLessonComplete, toggleBookmark, saveNote } = useProgress()
  const [activeTab, setActiveTab] = useState<'lesson' | 'diagrams' | 'summary' | 'terms'>('lesson')
  const [activeImageZoom, setActiveImageZoom] = useState<OriginalImage | null>(null)
  const [noteContent, setNoteContent] = useState<string>('')
  const [showNotesDrawer, setShowNotesDrawer] = useState(false)
  const [sidebarOpen, setSidebarOpen] = useState(false)

  const chapterIndex = CHAPTERS.findIndex(c => c.id === chapterId)
  const chapter = CHAPTERS[chapterIndex] || CHAPTERS[0]
  const currentLessonIndex = chapter.lessons.findIndex(l => l.id === lessonId)
  const currentLesson: Lesson = chapter.lessons[currentLessonIndex] || chapter.lessons[0]

  useEffect(() => {
    setNoteContent(progress.notes[currentLesson.id] || '')
  }, [currentLesson.id, progress.notes])

  useEffect(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }, [chapterId, lessonId])

  const isCompleted = progress.completedLessons.includes(currentLesson.id)
  const isBookmarked = progress.bookmarks.includes(currentLesson.id)

  const handleToggleComplete = () => {
    markLessonComplete(currentLesson.id, chapter.id)
  }

  const handleSaveNote = () => {
    saveNote(currentLesson.id, noteContent)
  }

  const handlePrev = () => {
    if (currentLessonIndex > 0) {
      onNavigateLesson(chapter.id, chapter.lessons[currentLessonIndex - 1].id)
    } else if (chapterIndex > 0) {
      const prevChapter = CHAPTERS[chapterIndex - 1]
      onNavigateLesson(prevChapter.id, prevChapter.lessons[prevChapter.lessons.length - 1].id)
    }
  }

  const handleNext = () => {
    markLessonComplete(currentLesson.id, chapter.id)
    if (currentLessonIndex < chapter.lessons.length - 1) {
      onNavigateLesson(chapter.id, chapter.lessons[currentLessonIndex + 1].id)
    } else if (chapterIndex < CHAPTERS.length - 1) {
      const nextChapter = CHAPTERS[chapterIndex + 1]
      onNavigateLesson(nextChapter.id, nextChapter.lessons[0].id)
    } else {
      onTakeQuiz(chapter.id)
    }
  }

  return (
    <div className="space-y-6 animate-in fade-in duration-300">
      <div className="flex items-center justify-between gap-3 pb-2 border-b border-slate-800">
        <button
          onClick={onBackToCurriculum}
          className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-slate-900/80 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-700/60 transition-colors text-xs sm:text-sm font-semibold touch-target"
        >
          <ArrowLeft className="w-4 h-4 text-emerald-400" />
          <span>กลับหน้าหลักสูตร</span>
        </button>

        <div className="flex items-center gap-2">
          <button
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="ipad:hidden px-3 py-2 rounded-xl bg-slate-900 text-slate-300 border border-slate-800 text-xs font-semibold touch-target flex items-center gap-1.5"
          >
            <BookOpen className="w-4 h-4 text-emerald-400" />
            <span>สารบัญ</span>
          </button>

          <button
            onClick={() => toggleBookmark(currentLesson.id)}
            className={`p-2 rounded-xl border transition-colors touch-target flex items-center justify-center ${
              isBookmarked
                ? 'bg-amber-500/20 text-amber-400 border-amber-500/30'
                : 'bg-slate-900/80 text-slate-400 border-slate-800 hover:text-white'
            }`}
            title="บุ๊กมาร์กบทเรียนนี้"
          >
            <Bookmark className={`w-4 h-4 ${isBookmarked ? 'fill-amber-400' : ''}`} />
          </button>

          <button
            onClick={() => setShowNotesDrawer(!showNotesDrawer)}
            className="px-3 py-2 rounded-xl bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 text-xs font-semibold touch-target flex items-center gap-1.5"
          >
            <FileText className="w-4 h-4 text-emerald-400" />
            <span className="hidden sm:inline">สมุดจด</span>
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 ipad:grid-cols-12 gap-6">
        <aside className={`ipad:col-span-4 lg:col-span-3 space-y-4 ${
          sidebarOpen ? 'block' : 'hidden ipad:block'
        }`}>
          <div className="glass-card p-4 sm:p-5 rounded-2xl border border-slate-800 sticky top-24 max-h-[calc(100dvh-120px)] overflow-y-auto">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-extrabold uppercase tracking-wider text-emerald-400">
                บทที่ {chapter.chapterNumber}: สารบัญบท
              </span>
              <span className="text-[11px] text-slate-400">
                หน้า {chapter.pdfPages}
              </span>
            </div>

            <h3 className="text-sm font-bold text-white mb-4 leading-snug">
              {chapter.title}
            </h3>

            <div className="space-y-1.5 mb-6">
              {chapter.lessons.map((les, idx) => {
                const isCur = les.id === currentLesson.id
                const isLesDone = progress.completedLessons.includes(les.id)
                return (
                  <button
                    key={les.id}
                    onClick={() => {
                      onNavigateLesson(chapter.id, les.id)
                      setSidebarOpen(false)
                    }}
                    className={`w-full text-left p-2.5 rounded-xl text-xs font-medium transition-all flex items-start gap-2.5 touch-target ${
                      isCur
                        ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                        : 'text-slate-300 hover:bg-slate-800/80'
                    }`}
                  >
                    <span className={`w-5 h-5 rounded-full flex items-center justify-center shrink-0 text-[10px] font-bold ${
                      isLesDone
                        ? 'bg-emerald-500 text-slate-950'
                        : isCur
                        ? 'bg-emerald-500/30 text-emerald-400 border border-emerald-500/40'
                        : 'bg-slate-800 text-slate-400'
                    }`}>
                      {isLesDone ? <CheckCircle2 className="w-3 h-3 stroke-[3]" /> : idx + 1}
                    </span>
                    <span className="leading-snug pt-0.5 line-clamp-2">
                      {les.title}
                    </span>
                  </button>
                )
              })}
            </div>

            <div className="pt-4 border-t border-slate-800 space-y-2">
              <button
                onClick={() => onTakeQuiz(chapter.id)}
                className="w-full flex items-center justify-center gap-2 py-2.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 text-slate-950 font-bold text-xs shadow-md shadow-emerald-500/20 touch-target"
              >
                <Award className="w-4 h-4 stroke-[2.5]" />
                <span>ทำแบบทดสอบประจำบท</span>
              </button>
            </div>
          </div>
        </aside>

        <main className="ipad:col-span-8 lg:col-span-9 space-y-6">
          <div className="glass-card p-6 sm:p-8 rounded-3xl border border-slate-800 space-y-4">
            <div className="flex flex-wrap items-center gap-2 text-xs">
              <span className="px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 font-bold border border-emerald-500/20">
                บทที่ {chapter.chapterNumber}
              </span>
              <span className="text-slate-400">PDF Trade.pdf หน้า {chapter.pdfPages}</span>
              <span className="text-slate-500">•</span>
              <span className="text-slate-400 flex items-center gap-1">
                <Clock className="w-3.5 h-3.5" /> {chapter.estimatedMinutes} นาที
              </span>
              <span className="text-slate-500">•</span>
              <span className="text-emerald-400/90 font-medium">{chapter.category}</span>
            </div>

            <h1 className="text-xl sm:text-2xl lg:text-3xl font-extrabold text-white tracking-tight leading-tight">
              {currentLesson.title}
            </h1>
            <p className="text-xs sm:text-sm font-mono text-emerald-400/80">
              {chapter.englishTitle}
            </p>

            <div className="flex items-center gap-2 pt-2 border-b border-slate-800/80 overflow-x-auto">
              {[
                { id: 'lesson', label: 'เนื้อหาบทเรียน' },
                { id: 'diagrams', label: `ภาพกราฟและผังแท้จริง (${chapter.originalImages.length})` },
                { id: 'summary', label: 'สรุปหัวใจสำคัญ' },
                { id: 'terms', label: `คำศัพท์สำคัญ (${chapter.keyTerms.length})` }
              ].map(tab => (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id as any)}
                  className={`px-4 py-2 text-xs sm:text-sm font-semibold whitespace-nowrap transition-all border-b-2 -mb-[2px] touch-target ${
                    activeTab === tab.id
                      ? 'border-emerald-400 text-emerald-400 bg-emerald-500/5'
                      : 'border-transparent text-slate-400 hover:text-slate-200'
                  }`}
                >
                  {tab.label}
                </button>
              ))}
            </div>

            {activeTab === 'lesson' && (
              <div className="space-y-6 pt-2">
                <div className="p-4 sm:p-5 rounded-2xl bg-slate-900/70 border border-slate-800/90 space-y-2">
                  <div className="flex items-center gap-2 text-xs font-bold text-amber-400">
                    <Sparkles className="w-4 h-4" />
                    <span>ทำไมหัวข้อนี้จึงสำคัญยิ่งยวดในการเทรด Forex?</span>
                  </div>
                  <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                    {chapter.whyItMatters}
                  </p>
                </div>

                <div className="prose prose-invert max-w-none space-y-4 text-slate-200 text-sm sm:text-base leading-relaxed whitespace-pre-line font-normal">
                  {currentLesson.content}
                </div>

                {currentLesson.corePrinciples && currentLesson.corePrinciples.length > 0 && (
                  <div className="p-5 rounded-2xl bg-slate-900/90 border border-emerald-500/30 space-y-3">
                    <div className="flex items-center gap-2 text-sm font-bold text-emerald-400">
                      <CheckCircle2 className="w-4 h-4" />
                      <span>กฎเหล็กและหลักการที่ต้องจดจำ (Core Rules)</span>
                    </div>
                    <ul className="space-y-2">
                      {currentLesson.corePrinciples.map((rule, idx) => (
                        <li key={idx} className="flex items-start gap-2.5 text-xs sm:text-sm text-slate-200">
                          <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-2 shrink-0" />
                          <span>{rule}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {currentLesson.practicalExamples && (
                  <div className="p-5 rounded-2xl bg-blue-950/20 border border-blue-500/30 space-y-2">
                    <div className="flex items-center gap-2 text-sm font-bold text-blue-400">
                      <Lightbulb className="w-4 h-4" />
                      <span>ตัวอย่างการใช้งานจริงในตลาด Forex (Practical Setup)</span>
                    </div>
                    <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                      {currentLesson.practicalExamples}
                    </p>
                  </div>
                )}

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {currentLesson.proTips && (
                    <div className="p-4 rounded-xl bg-emerald-950/20 border border-emerald-500/20 space-y-1.5">
                      <div className="flex items-center gap-2 text-xs font-bold text-emerald-400">
                        <Sparkles className="w-3.5 h-3.5" />
                        <span>เคล็ดลับสถาบัน (Smart Money Pro Tip)</span>
                      </div>
                      <p className="text-xs text-slate-300 leading-relaxed">
                        {currentLesson.proTips}
                      </p>
                    </div>
                  )}

                  {currentLesson.pitfalls && (
                    <div className="p-4 rounded-xl bg-rose-950/20 border border-rose-500/20 space-y-1.5">
                      <div className="flex items-center gap-2 text-xs font-bold text-rose-400">
                        <ShieldAlert className="w-3.5 h-3.5" />
                        <span>กับดักรายย่อยที่ต้องระวัง (Retail Trap)</span>
                      </div>
                      <p className="text-xs text-slate-300 leading-relaxed">
                        {currentLesson.pitfalls}
                      </p>
                    </div>
                  )}
                </div>

                {chapter.originalImages.length > 0 && (
                  <div className="space-y-3 pt-4 border-t border-slate-800">
                    <div className="flex items-center justify-between">
                      <h4 className="text-sm font-bold text-white flex items-center gap-2">
                        <Layers className="w-4 h-4 text-emerald-400" />
                        <span>ภาพกราฟจริงจาก E-Book สำหรับบทนี้</span>
                      </h4>
                      <button
                        onClick={() => setActiveTab('diagrams')}
                        className="text-xs text-emerald-400 hover:text-emerald-300 font-semibold"
                      >
                        ดูภาพขนาดใหญ่ทั้งหมด
                      </button>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                      {chapter.originalImages.slice(0, 2).map((img, i) => (
                        <div
                          key={i}
                          onClick={() => setActiveImageZoom(img)}
                          className="group relative rounded-xl overflow-hidden bg-slate-900 border border-slate-800 cursor-pointer hover:border-emerald-500/50 transition-all"
                        >
                          <img
                            src={img.url}
                            alt={img.caption}
                            className="w-full h-48 sm:h-56 object-cover object-top group-hover:scale-105 transition-transform duration-300"
                            loading="lazy"
                          />
                          <div className="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-transparent to-transparent flex flex-col justify-end p-3">
                            <p className="text-[11px] font-medium text-white line-clamp-2">
                              {img.caption}
                            </p>
                            <span className="text-[10px] text-emerald-400 flex items-center gap-1 mt-1">
                              <ZoomIn className="w-3 h-3" /> แตะเพื่อขยายดูเต็มจอ
                            </span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {activeTab === 'diagrams' && (
              <div className="space-y-6 pt-2">
                <p className="text-xs text-slate-400">
                  รวมภาพและผังประกอบการสอนจริงจาก Trade.pdf ประจำบทเรียนนี้ สามารถแตะที่ภาพเพื่อขยายดูรายละเอียดแท่งเทียนได้
                </p>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {chapter.originalImages.map((img, i) => (
                    <div
                      key={i}
                      onClick={() => setActiveImageZoom(img)}
                      className="group glass-card rounded-2xl overflow-hidden border border-slate-800 hover:border-emerald-500/50 cursor-pointer transition-all flex flex-col"
                    >
                      <div className="relative bg-slate-950 aspect-[4/3] flex items-center justify-center overflow-hidden">
                        <img
                          src={img.url}
                          alt={img.caption}
                          className="w-full h-full object-contain group-hover:scale-105 transition-transform duration-300"
                          loading="lazy"
                        />
                        <div className="absolute top-2 right-2 px-2 py-1 rounded-md bg-slate-900/80 backdrop-blur-md text-[10px] font-bold text-emerald-400 border border-slate-700/60 flex items-center gap-1">
                          <ZoomIn className="w-3 h-3" /> ขยาย
                        </div>
                      </div>
                      <div className="p-3 bg-slate-900/90 border-t border-slate-800">
                        <p className="text-xs font-medium text-slate-200">
                          {img.caption}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {activeTab === 'summary' && (
              <div className="space-y-4 pt-2">
                <div className="p-5 rounded-2xl bg-slate-900/80 border border-slate-800 space-y-3">
                  <h4 className="text-sm font-bold text-white flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                    <span>สรุปหัวใจสำคัญของบทเรียน (Key Takeaways)</span>
                  </h4>
                  <ul className="space-y-2.5">
                    {chapter.summary.map((point, idx) => (
                      <li key={idx} className="flex items-start gap-2.5 text-xs sm:text-sm text-slate-300">
                        <span className="w-2 h-2 rounded-full bg-emerald-400 mt-1.5 shrink-0" />
                        <span className="leading-relaxed">{point}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            )}

            {activeTab === 'terms' && (
              <div className="space-y-4 pt-2">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  {chapter.keyTerms.map((term, idx) => (
                    <div key={idx} className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1">
                      <div className="font-bold text-sm text-emerald-400 font-mono">
                        {term.term}
                      </div>
                      <p className="text-xs text-slate-300 leading-relaxed">
                        {term.meaning}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            <div className="pt-6 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div className="flex items-center gap-2 w-full sm:w-auto">
                <button
                  onClick={handlePrev}
                  className="flex-1 sm:flex-initial flex items-center justify-center gap-1.5 px-4 py-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-800 text-xs sm:text-sm font-semibold transition-colors touch-target"
                >
                  <ChevronLeft className="w-4 h-4" />
                  <span>บทเรียนก่อนหน้า</span>
                </button>

                <button
                  onClick={handleToggleComplete}
                  className={`flex-1 sm:flex-initial flex items-center justify-center gap-1.5 px-4 py-3 rounded-xl border text-xs sm:text-sm font-semibold transition-all touch-target ${
                    isCompleted
                      ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/40'
                      : 'bg-slate-900 hover:bg-slate-800 text-slate-400 border-slate-800'
                  }`}
                >
                  <CheckCircle2 className="w-4 h-4" />
                  <span>{isCompleted ? 'เรียนจบแล้ว' : 'ทำเครื่องหมายว่าเรียนแล้ว'}</span>
                </button>
              </div>

              <div className="flex items-center gap-2 w-full sm:w-auto">
                <button
                  onClick={handleNext}
                  className="w-full sm:w-auto flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-400 hover:to-emerald-500 text-slate-950 font-bold text-xs sm:text-sm shadow-md shadow-emerald-500/20 transition-all touch-target"
                >
                  <span>
                    {currentLessonIndex < chapter.lessons.length - 1
                      ? 'บทเรียนถัดไป'
                      : chapterIndex < CHAPTERS.length - 1
                      ? 'ขึ้นบทถัดไป'
                      : 'ทำแบบทดสอบประจำบท'}
                  </span>
                  <ChevronRight className="w-4 h-4 stroke-[2.5]" />
                </button>
              </div>
            </div>
          </div>
        </main>
      </div>

      {showNotesDrawer && (
        <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex justify-end">
          <div className="w-full max-w-md bg-slate-900 border-l border-slate-800 h-full p-6 flex flex-col justify-between animate-in slide-in-from-right duration-300">
            <div className="space-y-4">
              <div className="flex items-center justify-between pb-3 border-b border-slate-800">
                <div className="flex items-center gap-2 text-white font-bold text-base">
                  <FileText className="w-5 h-5 text-emerald-400" />
                  <span>สมุดบันทึกส่วนตัว</span>
                </div>
                <button
                  onClick={() => setShowNotesDrawer(false)}
                  className="p-1 rounded-lg text-slate-400 hover:text-white"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              <p className="text-xs text-slate-400">
                บันทึกข้อคิด ความเข้าใจ หรือข้อสงสัยประจำบทเรียน: <span className="text-slate-200 font-semibold">{currentLesson.title}</span>
              </p>

              <textarea
                value={noteContent}
                onChange={e => setNoteContent(e.target.value)}
                placeholder="พิมพ์บันทึกของคุณที่นี่ ข้อมูลจะถูกบันทึกอัตโนมัติบนอุปกรณ์ของคุณ..."
                rows={12}
                className="w-full p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 text-sm focus:outline-none focus:border-emerald-500 transition-colors resize-none leading-relaxed"
              />
            </div>

            <div className="flex items-center gap-3 pt-4 border-t border-slate-800">
              <button
                onClick={() => {
                  handleSaveNote()
                  setShowNotesDrawer(false)
                }}
                className="flex-1 py-3 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-sm shadow-md transition-colors touch-target"
              >
                บันทึกโน้ต
              </button>
              <button
                onClick={() => setShowNotesDrawer(false)}
                className="px-4 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-semibold transition-colors touch-target"
              >
                ปิด
              </button>
            </div>
          </div>
        </div>
      )}

      {activeImageZoom && (
        <div
          onClick={() => setActiveImageZoom(null)}
          className="fixed inset-0 z-50 bg-slate-950/95 backdrop-blur-md flex items-center justify-center p-4 animate-in fade-in duration-200"
        >
          <div
            onClick={e => e.stopPropagation()}
            className="relative max-w-5xl w-full max-h-[90dvh] flex flex-col bg-slate-900 border border-slate-800 rounded-3xl overflow-hidden shadow-2xl"
          >
            <div className="flex items-center justify-between p-4 border-b border-slate-800 bg-slate-900/80">
              <div>
                <h4 className="text-sm font-bold text-white">
                  {activeImageZoom.caption}
                </h4>
                <p className="text-[11px] text-slate-400">
                  Trade.pdf หน้า {activeImageZoom.page}
                </p>
              </div>
              <button
                onClick={() => setActiveImageZoom(null)}
                className="p-2 rounded-xl bg-slate-800 text-slate-400 hover:text-white transition-colors touch-target"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="flex-1 overflow-auto p-4 flex items-center justify-center bg-slate-950">
              <img
                src={activeImageZoom.url}
                alt={activeImageZoom.caption}
                className="max-w-full max-h-[75dvh] object-contain rounded-lg"
              />
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
