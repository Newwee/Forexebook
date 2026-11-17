import React, { useState } from 'react'
import { ProgressProvider, useProgress } from './context/ProgressContext'
import { Navbar } from './components/Navbar'
import { Dashboard } from './components/Dashboard'
import { CurriculumView } from './components/CurriculumView'
import { LessonReader } from './components/LessonReader'
import { QuizView } from './components/QuizView'
import { ScenarioSimulator } from './components/ScenarioSimulator'
import { GlossaryView } from './components/GlossaryView'
import { MistakesReview } from './components/MistakesReview'
import { SearchModal } from './components/SearchModal'
import { CHAPTERS } from './data/curriculum'
import {
  Compass,
  BookOpen,
  Target,
  Bookmark,
  AlertTriangle,
  FileText
} from 'lucide-react'

const AppContent: React.FC = () => {
  const { progress, setLastLesson } = useProgress()
  const [currentTab, setCurrentTab] = useState<string>('dashboard')
  const [activeChapterId, setActiveChapterId] = useState<string>('ch-01-forex-basics')
  const [activeLessonId, setActiveLessonId] = useState<string>('lesson-1-1')
  const [isSearchOpen, setIsSearchOpen] = useState(false)

  const handleStartLesson = (chapterId: string, lessonId: string) => {
    setActiveChapterId(chapterId)
    setActiveLessonId(lessonId)
    setLastLesson(lessonId)
    setCurrentTab('reader')
  }

  const handleTakeQuiz = (chapterId: string) => {
    setActiveChapterId(chapterId)
    setCurrentTab('quiz')
  }

  const handleNextChapter = (nextChapterId: string) => {
    const nextCh = CHAPTERS.find(c => c.id === nextChapterId)
    if (nextCh && nextCh.lessons.length > 0) {
      handleStartLesson(nextCh.id, nextCh.lessons[0].id)
    } else {
      setCurrentTab('curriculum')
    }
  }

  return (
    <div className="min-h-[100dvh] flex flex-col bg-navy-950 text-slate-100 selection:bg-emerald-500/30 selection:text-emerald-300">
      <Navbar
        currentTab={currentTab}
        setCurrentTab={setCurrentTab}
        onOpenSearch={() => setIsSearchOpen(true)}
      />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8 pb-24 ipad:pb-12">
        {currentTab === 'dashboard' && (
          <Dashboard
            onStartLesson={handleStartLesson}
            onTakeQuiz={handleTakeQuiz}
            onGoToTab={setCurrentTab}
          />
        )}

        {currentTab === 'curriculum' && (
          <CurriculumView
            onSelectLesson={handleStartLesson}
            onTakeQuiz={handleTakeQuiz}
          />
        )}

        {currentTab === 'reader' && (
          <LessonReader
            chapterId={activeChapterId}
            lessonId={activeLessonId}
            onNavigateLesson={handleStartLesson}
            onTakeQuiz={handleTakeQuiz}
            onBackToCurriculum={() => setCurrentTab('curriculum')}
          />
        )}

        {currentTab === 'quiz' && (
          <QuizView
            chapterId={activeChapterId}
            onClose={() => setCurrentTab('curriculum')}
            onReviewChapter={chId => {
              const ch = CHAPTERS.find(c => c.id === chId)
              if (ch) handleStartLesson(ch.id, ch.lessons[0].id)
            }}
            onNextChapter={handleNextChapter}
          />
        )}

        {currentTab === 'simulator' && <ScenarioSimulator />}

        {currentTab === 'glossary' && (
          <GlossaryView
            onGoToLesson={chId => {
              const ch = CHAPTERS.find(c => c.id === chId)
              if (ch) handleStartLesson(ch.id, ch.lessons[0].id)
            }}
          />
        )}

        {currentTab === 'mistakes' && (
          <MistakesReview
            onGoToLesson={chId => {
              const ch = CHAPTERS.find(c => c.id === chId)
              if (ch) handleStartLesson(ch.id, ch.lessons[0].id)
            }}
            onRetakeQuiz={handleTakeQuiz}
          />
        )}
      </main>

      <div className="ipad:hidden fixed bottom-0 left-0 right-0 z-40 glass-panel border-t border-slate-800/80 px-2 py-1.5 flex items-center justify-around shadow-2xl safe-area-pb">
        {[
          { id: 'dashboard', label: 'แดชบอร์ด', icon: Compass },
          { id: 'curriculum', label: 'บทเรียน', icon: BookOpen },
          { id: 'simulator', label: 'จำลองเทรด', icon: Target },
          { id: 'glossary', label: 'คำศัพท์', icon: Bookmark },
          { id: 'mistakes', label: 'จุดอ่อน', icon: AlertTriangle }
        ].map(item => {
          const Icon = item.icon
          const isActive = currentTab === item.id
          return (
            <button
              key={item.id}
              onClick={() => setCurrentTab(item.id)}
              className={`flex flex-col items-center justify-center p-2 rounded-xl text-[10px] font-semibold transition-all touch-target ${
                isActive ? 'text-emerald-400 font-bold' : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <Icon className={`w-5 h-5 mb-0.5 ${isActive ? 'text-emerald-400' : 'text-slate-400'}`} />
              <span>{item.label}</span>
            </button>
          )
        })}
      </div>

      <footer className="w-full border-t border-slate-900 bg-navy-950 py-6 text-center text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <span className="font-bold text-slate-400">SMC WARRIORS TRADER E-BOOK</span>
            <span>•</span>
            <span>Based on Trade.pdf (116 Pages Source of Truth)</span>
          </div>
          <div>
            <span>ออกแบบสำหรับ iPad, Tablet, Mobile & Desktop</span>
          </div>
        </div>
      </footer>

      <SearchModal
        isOpen={isSearchOpen}
        onClose={() => setIsSearchOpen(false)}
        onSelectLesson={handleStartLesson}
        onSelectGlossary={() => setCurrentTab('glossary')}
      />
    </div>
  )
}

export const App: React.FC = () => {
  return (
    <ProgressProvider>
      <AppContent />
    </ProgressProvider>
  )
}

export default App
