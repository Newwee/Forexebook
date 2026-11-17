import React, { useState } from 'react'
import {
  BookOpen,
  Compass,
  Bookmark,
  Award,
  Zap,
  Flame,
  Search,
  Menu,
  X,
  Target,
  AlertTriangle,
  RotateCcw
} from 'lucide-react'
import { useProgress } from '../context/ProgressContext'
import { CHAPTERS } from '../data/curriculum'

interface NavbarProps {
  currentTab: string
  setCurrentTab: (tab: string) => void
  onOpenSearch: () => void
}

export const Navbar: React.FC<NavbarProps> = ({
  currentTab,
  setCurrentTab,
  onOpenSearch
}) => {
  const { progress } = useProgress()
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  const totalLessons = CHAPTERS.reduce((acc, ch) => acc + ch.lessons.length, 0)
  const completedCount = progress.completedLessons.length
  const progressPercent = Math.round((completedCount / totalLessons) * 100) || 0

  const navItems = [
    { id: 'dashboard', label: 'แดชบอร์ด', icon: Compass },
    { id: 'curriculum', label: 'หลักสูตร SMC', icon: BookOpen },
    { id: 'simulator', label: 'จำลองการเทรด', icon: Target },
    { id: 'glossary', label: 'คลังคำศัพท์', icon: Bookmark },
    { id: 'mistakes', label: 'ทบทวนจุดอ่อน', icon: AlertTriangle, badge: Object.keys(progress.incorrectQuestions).length }
  ]

  const handleSelectTab = (id: string) => {
    setCurrentTab(id)
    setMobileMenuOpen(false)
  }

  return (
    <header className="sticky top-0 z-40 w-full glass-panel border-b border-slate-800/80 transition-all">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16 sm:h-20">
          <div
            onClick={() => handleSelectTab('dashboard')}
            className="flex items-center gap-3 cursor-pointer group select-none"
          >
            <div className="w-10 h-10 sm:w-11 sm:h-11 rounded-xl bg-gradient-to-br from-emerald-400 to-emerald-600 flex items-center justify-center shadow-lg shadow-emerald-500/20 group-hover:scale-105 transition-transform">
              <Zap className="w-5 h-5 sm:w-6 sm:h-6 text-slate-950 stroke-[2.5]" />
            </div>
            <div>
              <div className="flex items-center gap-1.5">
                <span className="font-extrabold text-lg sm:text-xl tracking-tight text-white group-hover:text-emerald-400 transition-colors">
                  SMC WARRIORS
                </span>
                <span className="px-1.5 py-0.5 text-[10px] font-bold uppercase tracking-wider rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                  PRO
                </span>
              </div>
              <p className="text-[11px] text-slate-400 font-medium hidden sm:block">
                Interactive Smart Money Forex Platform
              </p>
            </div>
          </div>

          <nav className="hidden ipad:flex items-center gap-1 lg:gap-2">
            {navItems.map(item => {
              const Icon = item.icon
              const isActive = currentTab === item.id
              return (
                <button
                  key={item.id}
                  onClick={() => handleSelectTab(item.id)}
                  className={`relative flex items-center gap-2 px-3.5 py-2 rounded-xl text-sm font-semibold transition-all touch-target ${
                    isActive
                      ? 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30 shadow-sm'
                      : 'text-slate-300 hover:text-white hover:bg-slate-800/60 border border-transparent'
                  }`}
                >
                  <Icon className={`w-4 h-4 ${isActive ? 'text-emerald-400' : 'text-slate-400'}`} />
                  <span>{item.label}</span>
                  {Boolean(item.badge && item.badge > 0) && (
                    <span className="ml-1 px-1.5 py-0.2 text-[10px] font-bold rounded-full bg-rose-500/20 text-rose-400 border border-rose-500/30">
                      {item.badge}
                    </span>
                  )}
                </button>
              )
            })}
          </nav>

          <div className="flex items-center gap-2.5 sm:gap-4">
            <button
              onClick={onOpenSearch}
              className="flex items-center gap-2 px-3 py-2 rounded-xl bg-slate-900/80 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-700/60 transition-colors touch-target text-xs sm:text-sm font-medium"
              title="ค้นหาคำศัพท์หรือบทเรียน"
            >
              <Search className="w-4 h-4 text-emerald-400" />
              <span className="hidden md:inline">ค้นหา</span>
              <kbd className="hidden lg:inline-block px-1.5 py-0.5 text-[10px] bg-slate-800 border border-slate-700 rounded text-slate-400 font-mono">
                ⌘K
              </kbd>
            </button>

            <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-900/80 border border-slate-800 text-amber-400 font-bold text-xs sm:text-sm shadow-inner">
              <Flame className="w-4 h-4 text-amber-400 animate-pulse fill-amber-400/30" />
              <span>{progress.streak}</span>
              <span className="text-[11px] text-slate-400 font-normal hidden xs:inline">วัน</span>
            </div>

            <div className="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900/80 border border-slate-800">
              <div className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse" />
              <span className="text-xs font-semibold text-slate-300">{progressPercent}%</span>
            </div>

            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="ipad:hidden p-2 rounded-xl bg-slate-900 text-slate-300 hover:text-white border border-slate-800 touch-target flex items-center justify-center"
              aria-label="Toggle menu"
            >
              {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>
          </div>
        </div>
      </div>

      {mobileMenuOpen && (
        <div className="ipad:hidden glass-panel border-b border-slate-800 px-4 pt-2 pb-4 space-y-1 animate-in slide-in-from-top duration-200">
          {navItems.map(item => {
            const Icon = item.icon
            const isActive = currentTab === item.id
            return (
              <button
                key={item.id}
                onClick={() => handleSelectTab(item.id)}
                className={`w-full flex items-center justify-between px-4 py-3 rounded-xl text-sm font-semibold transition-all touch-target ${
                  isActive
                    ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
                    : 'text-slate-300 hover:bg-slate-800/80'
                }`}
              >
                <div className="flex items-center gap-3">
                  <Icon className="w-5 h-5" />
                  <span>{item.label}</span>
                </div>
                {Boolean(item.badge && item.badge > 0) && (
                  <span className="px-2 py-0.5 text-xs font-bold rounded-full bg-rose-500/20 text-rose-400 border border-rose-500/30">
                    {item.badge}
                  </span>
                )}
              </button>
            )
          })}
        </div>
      )}
    </header>
  )
}
