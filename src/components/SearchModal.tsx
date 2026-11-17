import React, { useState, useEffect } from 'react'
import {
  Search,
  X,
  BookOpen,
  Bookmark,
  ArrowRight
} from 'lucide-react'
import { CHAPTERS, GLOSSARY_TERMS } from '../data/curriculum'

interface SearchModalProps {
  isOpen: boolean
  onClose: () => void
  onSelectLesson: (chapterId: string, lessonId: string) => void
  onSelectGlossary: () => void
}

export const SearchModal: React.FC<SearchModalProps> = ({
  isOpen,
  onClose,
  onSelectLesson,
  onSelectGlossary
}) => {
  const [query, setQuery] = useState('')

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault()
        if (isOpen) onClose()
        else {
          setQuery('')
        }
      }
      if (e.key === 'Escape' && isOpen) {
        onClose()
      }
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [isOpen, onClose])

  if (!isOpen) return null

  const q = query.toLowerCase().trim()

  const matchedChapters = q
    ? CHAPTERS.filter(ch =>
        ch.title.toLowerCase().includes(q) ||
        ch.englishTitle.toLowerCase().includes(q) ||
        ch.shortDescription.toLowerCase().includes(q) ||
        ch.lessons.some(l => l.title.toLowerCase().includes(q) || l.content.toLowerCase().includes(q))
      ).slice(0, 5)
    : []

  const matchedTerms = q
    ? GLOSSARY_TERMS.filter(term =>
        term.term.toLowerCase().includes(q) ||
        term.thaiName.toLowerCase().includes(q) ||
        term.definition.toLowerCase().includes(q)
      ).slice(0, 6)
    : []

  return (
    <div
      onClick={onClose}
      className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-start justify-center pt-16 sm:pt-24 px-4 animate-in fade-in duration-200"
    >
      <div
        onClick={e => e.stopPropagation()}
        className="w-full max-w-2xl bg-slate-900 border border-slate-700/80 rounded-3xl shadow-2xl overflow-hidden flex flex-col max-h-[80dvh] animate-in zoom-in-95 duration-200"
      >
        <div className="p-4 border-b border-slate-800 flex items-center gap-3">
          <Search className="w-5 h-5 text-emerald-400 shrink-0" />
          <input
            type="text"
            autoFocus
            value={query}
            onChange={e => setQuery(e.target.value)}
            placeholder="ค้นหาทุกสิ่ง: IDM, BOS, FVG, Lot, Spread, วินัย..."
            className="flex-1 bg-transparent text-white placeholder-slate-500 text-sm sm:text-base focus:outline-none"
          />
          {query && (
            <button
              onClick={() => setQuery('')}
              className="p-1 rounded-lg text-slate-400 hover:text-white"
            >
              <X className="w-4 h-4" />
            </button>
          )}
          <kbd className="hidden sm:inline-block px-2 py-0.5 text-[10px] bg-slate-800 border border-slate-700 rounded text-slate-400 font-mono">
            ESC
          </kbd>
        </div>

        <div className="flex-1 overflow-y-auto p-4 space-y-5">
          {!q && (
            <div className="py-8 text-center space-y-2">
              <p className="text-xs sm:text-sm text-slate-400">
                พิมพ์คำค้นหาเพื่อสำรวจบทเรียน 16 บท หรือคลังคำศัพท์ 35+ คำ
              </p>
              <div className="flex flex-wrap items-center justify-center gap-1.5 pt-2">
                {['IDM', 'Valid Pullback', 'BOS', 'SCOB', 'FVG', 'Order Flow', 'Premium/Discount'].map(tag => (
                  <button
                    key={tag}
                    onClick={() => setQuery(tag)}
                    className="px-2.5 py-1 rounded-lg bg-slate-800/80 text-xs text-slate-300 hover:text-emerald-400 border border-slate-700/60"
                  >
                    {tag}
                  </button>
                ))}
              </div>
            </div>
          )}

          {matchedChapters.length > 0 && (
            <div className="space-y-2">
              <span className="text-[11px] font-bold uppercase tracking-wider text-emerald-400 px-2">
                บทเรียนที่เกี่ยวข้อง ({matchedChapters.length})
              </span>
              <div className="space-y-1">
                {matchedChapters.map(ch => (
                  <div
                    key={ch.id}
                    onClick={() => {
                      onSelectLesson(ch.id, ch.lessons[0].id)
                      onClose()
                    }}
                    className="p-3 rounded-2xl bg-slate-800/40 hover:bg-slate-800/90 border border-slate-800/60 hover:border-emerald-500/30 cursor-pointer transition-all flex items-center justify-between"
                  >
                    <div className="space-y-0.5">
                      <div className="flex items-center gap-2">
                        <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                          บทที่ {ch.chapterNumber}
                        </span>
                        <h4 className="text-xs sm:text-sm font-bold text-white">
                          {ch.title}
                        </h4>
                      </div>
                      <p className="text-[11px] text-slate-400 line-clamp-1">
                        {ch.shortDescription}
                      </p>
                    </div>
                    <ArrowRight className="w-4 h-4 text-slate-500 shrink-0 ml-3" />
                  </div>
                ))}
              </div>
            </div>
          )}

          {matchedTerms.length > 0 && (
            <div className="space-y-2">
              <span className="text-[11px] font-bold uppercase tracking-wider text-blue-400 px-2">
                คำศัพท์ที่เกี่ยวข้อง ({matchedTerms.length})
              </span>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                {matchedTerms.map(term => (
                  <div
                    key={term.id}
                    onClick={() => {
                      onSelectGlossary()
                      onClose()
                    }}
                    className="p-3 rounded-xl bg-slate-800/40 hover:bg-slate-800/90 border border-slate-800/60 cursor-pointer transition-all space-y-1"
                  >
                    <div className="font-bold text-xs text-white flex items-center justify-between">
                      <span className="text-emerald-400">{term.term}</span>
                      <span className="text-[10px] text-slate-400">{term.category}</span>
                    </div>
                    <p className="text-[11px] text-slate-300 line-clamp-2">
                      {term.definition}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {q && matchedChapters.length === 0 && matchedTerms.length === 0 && (
            <div className="py-10 text-center text-slate-400 text-xs sm:text-sm">
              ไม่พบผลลัพธ์ที่ตรงกับ "{query}" กรุณาลองใช้คำค้นหาอื่น
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
