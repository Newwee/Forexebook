import React, { useState } from 'react'
import {
  Target,
  CheckCircle2,
  XCircle,
  HelpCircle,
  ArrowRight,
  ZoomIn,
  X,
  Sparkles,
  ShieldCheck,
  RotateCcw,
  BookOpen
} from 'lucide-react'
import { PRACTICAL_SCENARIOS } from '../data/curriculum'
import { useProgress } from '../context/ProgressContext'
import { Scenario } from '../types'

export const ScenarioSimulator: React.FC = () => {
  const { progress, recordScenarioResult } = useProgress()
  const [selectedScenarioIndex, setSelectedScenarioIndex] = useState(0)
  const [selectedOptionId, setSelectedOptionId] = useState<string | null>(null)
  const [isAnswered, setIsAnswered] = useState(false)
  const [zoomChartUrl, setZoomChartUrl] = useState<string | null>(null)

  const currentScenario: Scenario = PRACTICAL_SCENARIOS[selectedScenarioIndex] || PRACTICAL_SCENARIOS[0]
  const isPreviouslyCompleted = progress.scenarioResults[currentScenario.id]

  const handleSelectOption = (optId: string) => {
    if (isAnswered) return
    setSelectedOptionId(optId)
  }

  const handleSubmit = () => {
    if (!selectedOptionId) return
    setIsAnswered(true)
    const opt = currentScenario.options.find(o => o.id === selectedOptionId)
    if (opt) {
      recordScenarioResult(currentScenario.id, opt.isCorrect)
    }
  }

  const handleResetCurrent = () => {
    setSelectedOptionId(null)
    setIsAnswered(false)
  }

  const handleNext = () => {
    if (selectedScenarioIndex < PRACTICAL_SCENARIOS.length - 1) {
      setSelectedScenarioIndex(prev => prev + 1)
      setSelectedOptionId(null)
      setIsAnswered(false)
    }
  }

  const selectedOptObj = currentScenario.options.find(o => o.id === selectedOptionId)

  return (
    <div className="space-y-6 sm:space-y-8 animate-in fade-in duration-300">
      <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-semibold mb-2">
            <Target className="w-3.5 h-3.5" />
            <span>Interactive Trading Simulator</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            ห้องทดลองจำลองสถานการณ์กราฟจริง (SMC Simulator)
          </h1>
          <p className="text-xs sm:text-sm text-slate-400 mt-1">
            ฝึกฝนการตัดสินใจและอ่านพฤติกรรมสถาบันจากกราฟจริงใน E-Book แบบไม่มีความเสี่ยง
          </p>
        </div>

        <div className="px-3.5 py-2 rounded-xl bg-slate-900/80 border border-slate-800 text-[11px] text-amber-400/90 flex items-center gap-2 max-w-md">
          <ShieldCheck className="w-4 h-4 shrink-0 text-amber-400" />
          <span>แบบฝึกหัดนี้สร้างขึ้นเพื่อการศึกษาเท่านั้น ไม่ใช่สัญญาณการเทรดสด</span>
        </div>
      </div>

      <div className="flex items-center gap-2 overflow-x-auto pb-2">
        {PRACTICAL_SCENARIOS.map((sc, idx) => {
          const isDone = progress.scenarioResults[sc.id]
          const isSelected = idx === selectedScenarioIndex
          return (
            <button
              key={sc.id}
              onClick={() => {
                setSelectedScenarioIndex(idx)
                setSelectedOptionId(null)
                setIsAnswered(false)
              }}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all touch-target ${
                isSelected
                  ? 'bg-emerald-500 text-slate-950 shadow-md shadow-emerald-500/25'
                  : 'bg-slate-900/80 text-slate-300 hover:bg-slate-800 border border-slate-800'
              }`}
            >
              <span>เคส {idx + 1}</span>
              {isDone !== undefined && (
                <span className={`w-2 h-2 rounded-full ${isDone ? 'bg-emerald-400' : 'bg-rose-400'}`} />
              )}
            </button>
          )
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <div className="lg:col-span-6 space-y-4">
          <div className="glass-card rounded-3xl overflow-hidden border border-slate-800 flex flex-col">
            <div className="p-4 bg-slate-900/80 border-b border-slate-800 flex items-center justify-between">
              <div className="flex items-center gap-2 text-xs text-slate-300">
                <BookOpen className="w-4 h-4 text-emerald-400" />
                <span className="font-semibold">ผังอ้างอิง: E-Book หน้า {currentScenario.originalPageRef}</span>
              </div>
              <button
                onClick={() => setZoomChartUrl(currentScenario.chartRenderUrl)}
                className="text-xs text-emerald-400 hover:text-emerald-300 flex items-center gap-1 font-semibold touch-target"
              >
                <ZoomIn className="w-3.5 h-3.5" />
                <span>ขยายกราฟ</span>
              </button>
            </div>

            <div
              onClick={() => setZoomChartUrl(currentScenario.chartRenderUrl)}
              className="relative bg-slate-950 aspect-[4/3] flex items-center justify-center p-2 cursor-pointer group"
            >
              <img
                src={currentScenario.chartRenderUrl}
                alt={currentScenario.title}
                className="max-h-full max-w-full object-contain group-hover:scale-[1.02] transition-transform duration-300"
              />
              <div className="absolute inset-0 bg-slate-950/20 group-hover:bg-transparent transition-colors flex items-center justify-center">
                <span className="opacity-0 group-hover:opacity-100 px-3 py-1.5 rounded-lg bg-slate-900/90 text-white text-xs font-semibold backdrop-blur-md border border-slate-700 transition-opacity">
                  แตะเพื่อดูแบบเต็มจอ
                </span>
              </div>
            </div>

            <div className="p-4 sm:p-5 bg-slate-900/60 border-t border-slate-800 space-y-2">
              <span className="text-[11px] font-bold uppercase tracking-wider text-emerald-400">
                โจทย์และบริบทตลาด (Market Context)
              </span>
              <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
                {currentScenario.setupDescription}
              </p>
            </div>
          </div>
        </div>

        <div className="lg:col-span-6 space-y-4">
          <div className="glass-card p-6 sm:p-7 rounded-3xl border border-slate-800 space-y-5">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="px-2.5 py-0.5 rounded-md bg-emerald-500/10 text-emerald-400 text-[11px] font-bold border border-emerald-500/20">
                  {currentScenario.category}
                </span>
                <span className="text-xs text-slate-400 font-mono">
                  ระดับ: {currentScenario.difficulty}
                </span>
              </div>
              <h2 className="text-base sm:text-lg font-bold text-white leading-snug">
                {currentScenario.title}
              </h2>
            </div>

            <div className="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 space-y-2">
              <div className="flex items-center gap-2 text-xs font-bold text-amber-400">
                <HelpCircle className="w-4 h-4" />
                <span>คำถามสำหรับการตัดสินใจ</span>
              </div>
              <p className="text-xs sm:text-sm text-slate-100 font-medium leading-relaxed">
                {currentScenario.question}
              </p>
            </div>

            <div className="space-y-3">
              {currentScenario.options.map((option, idx) => {
                const isSelected = selectedOptionId === option.id
                let btnStyle = 'bg-slate-900/70 border-slate-800 text-slate-200 hover:bg-slate-800 hover:border-slate-700'

                if (isAnswered) {
                  if (option.isCorrect) {
                    btnStyle = 'bg-emerald-950/40 border-emerald-500 text-emerald-200 shadow-md shadow-emerald-500/10'
                  } else if (isSelected && !option.isCorrect) {
                    btnStyle = 'bg-rose-950/40 border-rose-500 text-rose-200'
                  } else {
                    btnStyle = 'bg-slate-900/40 border-slate-800/60 text-slate-500 opacity-60'
                  }
                } else if (isSelected) {
                  btnStyle = 'bg-emerald-500/15 border-emerald-500 text-emerald-300 ring-1 ring-emerald-500'
                }

                return (
                  <button
                    key={option.id}
                    disabled={isAnswered}
                    onClick={() => handleSelectOption(option.id)}
                    className={`w-full text-left p-3.5 sm:p-4 rounded-2xl border transition-all flex items-start gap-3 touch-target ${btnStyle}`}
                  >
                    <span className={`w-6 h-6 rounded-lg flex items-center justify-center shrink-0 text-xs font-bold ${
                      isAnswered && option.isCorrect
                        ? 'bg-emerald-500 text-slate-950'
                        : isAnswered && isSelected && !option.isCorrect
                        ? 'bg-rose-500 text-white'
                        : isSelected
                        ? 'bg-emerald-500 text-slate-950'
                        : 'bg-slate-800 text-slate-400'
                    }`}>
                      {String.fromCharCode(65 + idx)}
                    </span>
                    <span className="text-xs sm:text-sm font-medium leading-relaxed pt-0.5">
                      {option.text}
                    </span>
                  </button>
                )
              })}
            </div>

            {isAnswered && selectedOptObj && (
              <div className={`p-5 rounded-2xl border space-y-3 animate-in slide-in-from-bottom-2 duration-300 ${
                selectedOptObj.isCorrect
                  ? 'bg-emerald-950/30 border-emerald-500/40'
                  : 'bg-rose-950/30 border-rose-500/40'
              }`}>
                <div className="flex items-center gap-2">
                  {selectedOptObj.isCorrect ? (
                    <>
                      <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                      <span className="font-bold text-sm text-emerald-400">การวิเคราะห์ของคุณเฉียบคมมาก!</span>
                    </>
                  ) : (
                    <>
                      <XCircle className="w-5 h-5 text-rose-400" />
                      <span className="font-bold text-sm text-rose-400">ยังไม่สอดคล้องกับพฤติกรรม Smart Money</span>
                    </>
                  )}
                </div>

                <p className="text-xs sm:text-sm text-slate-200 leading-relaxed">
                  {selectedOptObj.feedback}
                </p>

                <div className="pt-3 border-t border-slate-800/80 space-y-1.5">
                  <div className="flex items-center gap-2 text-xs font-bold text-emerald-400">
                    <Sparkles className="w-3.5 h-3.5" />
                    <span>คำอธิบายเชิงกลไกสถาบัน (Institutional Logic)</span>
                  </div>
                  <p className="text-xs text-slate-300 leading-relaxed">
                    {currentScenario.institutionalExplanation}
                  </p>
                </div>
              </div>
            )}

            <div className="pt-4 border-t border-slate-800 flex items-center justify-between">
              {isAnswered ? (
                <button
                  onClick={handleResetCurrent}
                  className="flex items-center gap-1.5 px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold touch-target"
                >
                  <RotateCcw className="w-3.5 h-3.5" />
                  <span>ลองตอบใหม่</span>
                </button>
              ) : (
                <span className="text-xs text-slate-500">เลือกคำตอบที่ดีที่สุด</span>
              )}

              {!isAnswered ? (
                <button
                  disabled={!selectedOptionId}
                  onClick={handleSubmit}
                  className={`px-6 py-3 rounded-xl font-bold text-xs sm:text-sm transition-all touch-target ${
                    selectedOptionId
                      ? 'bg-emerald-500 hover:bg-emerald-400 text-slate-950 shadow-md shadow-emerald-500/20'
                      : 'bg-slate-800 text-slate-500 cursor-not-allowed'
                  }`}
                >
                  ยืนยันการตัดสินใจ
                </button>
              ) : selectedScenarioIndex < PRACTICAL_SCENARIOS.length - 1 ? (
                <button
                  onClick={handleNext}
                  className="flex items-center gap-2 px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-400 text-slate-950 font-bold text-xs sm:text-sm shadow-md shadow-emerald-500/20 touch-target"
                >
                  <span>ไปเคสถัดไป (เคส {selectedScenarioIndex + 2})</span>
                  <ArrowRight className="w-4 h-4 stroke-[2.5]" />
                </button>
              ) : (
                <span className="text-xs font-bold text-emerald-400">คุณทำครบทุกสถานการณ์แล้ว!</span>
              )}
            </div>
          </div>
        </div>
      </div>

      {zoomChartUrl && (
        <div
          onClick={() => setZoomChartUrl(null)}
          className="fixed inset-0 z-50 bg-slate-950/95 backdrop-blur-md flex items-center justify-center p-4 animate-in fade-in duration-200"
        >
          <div
            onClick={e => e.stopPropagation()}
            className="relative max-w-5xl w-full max-h-[90dvh] flex flex-col bg-slate-900 border border-slate-800 rounded-3xl overflow-hidden shadow-2xl"
          >
            <div className="flex items-center justify-between p-4 border-b border-slate-800 bg-slate-900/80">
              <h4 className="text-sm font-bold text-white">
                {currentScenario.title} - กราฟจากหน้า {currentScenario.originalPageRef}
              </h4>
              <button
                onClick={() => setZoomChartUrl(null)}
                className="p-2 rounded-xl bg-slate-800 text-slate-400 hover:text-white transition-colors touch-target"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="flex-1 overflow-auto p-4 flex items-center justify-center bg-slate-950">
              <img
                src={zoomChartUrl}
                alt="Enlarged Chart"
                className="max-w-full max-h-[75dvh] object-contain rounded-lg"
              />
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
