import React, { useState } from 'react'
import {
  Search,
  Bookmark,
  BookOpen,
  ArrowRight,
  Filter,
  Sparkles,
  Layers
} from 'lucide-react'
import { GLOSSARY_TERMS, CHAPTERS } from '../data/curriculum'
import { Category } from '../types'

interface GlossaryViewProps {
  onGoToLesson: (chapterId: string) => void
}

export const GlossaryView: React.FC<GlossaryViewProps> = ({ onGoToLesson }) => {
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedCategory, setSelectedCategory] = useState<string>('All')

  const categories = [
    { id: 'All', label: 'ทั้งหมด' },
    { id: 'Foundations', label: 'พื้นฐาน Forex' },
    { id: 'Structure', label: 'โครงสร้างตลาด (Structure)' },
    { id: 'Liquidity', label: 'สภาพคล่อง (Liquidity)' },
    { id: 'Entry Execution', label: 'จุดเข้าเทรด (Execution)' },
    { id: 'Mastery', label: 'การบริหารพอร์ต (Management)' }
  ]

  const filteredTerms = GLOSSARY_TERMS.filter(item => {
    if (selectedCategory !== 'All' && item.category !== selectedCategory) return false
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase()
      const matchTerm = item.term.toLowerCase().includes(q)
      const matchThai = item.thaiName.toLowerCase().includes(q)
      const matchDef = item.definition.toLowerCase().includes(q)
      const matchEx = item.example.toLowerCase().includes(q)
      if (!matchTerm && !matchThai && !matchDef && !matchEx) return false
    }
    return true
  })

  return (
    <div className="space-y-6 sm:space-y-8 animate-in fade-in duration-300">
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-semibold mb-2">
            <Bookmark className="w-3.5 h-3.5" />
            <span>Forex & SMC Dictionary</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            คลังคำศัพท์และนิยามสถาบัน (Forex Glossary)
          </h1>
          <p className="text-xs sm:text-sm text-slate-400 mt-1">
            พจนานุกรมคำศัพท์สถาบัน {GLOSSARY_TERMS.length} คำที่สกัดจาก Trade.pdf พร้อมตัวอย่างการนำไปใช้จริง
          </p>
        </div>

        <div className="relative w-full md:w-80">
          <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            placeholder="ค้นหาคำศัพท์ เช่น Pip, IDM, FVG, Lot..."
            className="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-900/80 border border-slate-700/80 text-white placeholder-slate-500 text-xs sm:text-sm focus:outline-none focus:border-emerald-500 transition-colors"
          />
        </div>
      </div>

      <div className="flex items-center gap-2 overflow-x-auto pb-1">
        {categories.map(cat => (
          <button
            key={cat.id}
            onClick={() => setSelectedCategory(cat.id)}
            className={`px-3 py-1.5 rounded-xl text-xs font-semibold whitespace-nowrap transition-all touch-target ${
              selectedCategory === cat.id
                ? 'bg-emerald-500 text-slate-950 shadow-md shadow-emerald-500/20'
                : 'bg-slate-900/60 text-slate-300 hover:bg-slate-800 border border-slate-800'
            }`}
          >
            {cat.label}
          </button>
        ))}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
        {filteredTerms.map(item => {
          const relatedCh = CHAPTERS.find(c => c.id === item.relatedChapterId)

          return (
            <div
              key={item.id}
              className="glass-card rounded-2xl border border-slate-800 p-5 flex flex-col justify-between hover:border-emerald-500/40 transition-all group"
            >
              <div className="space-y-3">
                <div className="flex items-center justify-between gap-2">
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                    {item.category}
                  </span>
                  {relatedCh && (
                    <span className="text-[11px] text-slate-400 font-mono">
                      บทที่ {relatedCh.chapterNumber}
                    </span>
                  )}
                </div>

                <div>
                  <h3 className="text-base font-extrabold text-white group-hover:text-emerald-300 transition-colors tracking-tight">
                    {item.term}
                  </h3>
                  <p className="text-xs font-medium text-slate-400 mt-0.5">
                    {item.thaiName}
                  </p>
                </div>

                <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                  {item.definition}
                </p>

                <div className="p-3 rounded-xl bg-slate-900/80 border border-slate-800/80 space-y-1">
                  <div className="text-[10px] font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1">
                    <Sparkles className="w-3 h-3" />
                    <span>ตัวอย่างในตลาดจริง</span>
                  </div>
                  <p className="text-xs text-slate-300 leading-relaxed font-mono text-[11px]">
                    {item.example}
                  </p>
                </div>
              </div>

              {relatedCh && (
                <div className="pt-4 mt-4 border-t border-slate-800/80">
                  <button
                    onClick={() => onGoToLesson(relatedCh.id)}
                    className="w-full flex items-center justify-between text-xs font-semibold text-slate-300 hover:text-emerald-400 group-hover:text-emerald-400 transition-colors"
                  >
                    <span>เรียนรู้ใน: {relatedCh.title}</span>
                    <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
                  </button>
                </div>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}
