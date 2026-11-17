import React, { createContext, useContext, useState, useEffect } from 'react'
import { UserProgress, QuizAttempt, IncorrectQuestionRecord } from '../types'

const STORAGE_KEY = 'smc_warriors_learning_progress_v1'

const initialProgress: UserProgress = {
  completedLessons: [],
  completedChapters: [],
  quizScores: {},
  incorrectQuestions: {},
  weakTopics: [],
  bookmarks: [],
  notes: {},
  streak: 1,
  lastActiveDate: new Date().toISOString().split('T')[0],
  lastLessonId: 'lesson-1-1',
  scenarioResults: {}
}

interface ProgressContextType {
  progress: UserProgress
  markLessonComplete: (lessonId: string, chapterId: string) => void
  saveQuizScore: (
    chapterId: string,
    score: number,
    total: number,
    incorrects: Record<string, IncorrectQuestionRecord>,
    topic: string
  ) => void
  toggleBookmark: (lessonId: string) => void
  saveNote: (lessonId: string, noteText: string) => void
  recordScenarioResult: (scenarioId: string, isSuccess: boolean) => void
  setLastLesson: (lessonId: string) => void
  resetProgress: () => void
}

const ProgressContext = createContext<ProgressContextType | undefined>(undefined)

export const ProgressProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [progress, setProgress] = useState<UserProgress>(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY)
      if (saved) {
        const parsed = JSON.parse(saved)
        const today = new Date().toISOString().split('T')[0]
        if (parsed.lastActiveDate !== today) {
          const lastDate = new Date(parsed.lastActiveDate)
          const currDate = new Date(today)
          const diffDays = Math.round((currDate.getTime() - lastDate.getTime()) / (1000 * 3600 * 24))
          if (diffDays === 1) {
            parsed.streak = (parsed.streak || 0) + 1
          } else if (diffDays > 1) {
            parsed.streak = 1
          }
          parsed.lastActiveDate = today
        }
        return parsed
      }
    } catch (e) {
      console.error(e)
    }
    return initialProgress
  })

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(progress))
    } catch (e) {
      console.error(e)
    }
  }, [progress])

  const markLessonComplete = (lessonId: string, chapterId: string) => {
    setProgress(prev => {
      const nextCompleted = prev.completedLessons.includes(lessonId)
        ? prev.completedLessons
        : [...prev.completedLessons, lessonId]
      return {
        ...prev,
        completedLessons: nextCompleted,
        lastLessonId: lessonId
      }
    })
  }

  const saveQuizScore = (
    chapterId: string,
    score: number,
    total: number,
    incorrects: Record<string, IncorrectQuestionRecord>,
    topic: string
  ) => {
    const passed = (score / total) >= 0.8
    setProgress(prev => {
      const newScores: Record<string, QuizAttempt> = {
        ...prev.quizScores,
        [chapterId]: {
          score,
          total,
          date: new Date().toISOString(),
          passed
        }
      }
      const newChapters = passed && !prev.completedChapters.includes(chapterId)
        ? [...prev.completedChapters, chapterId]
        : prev.completedChapters

      const newIncorrects = { ...prev.incorrectQuestions, ...incorrects }
      let newWeakTopics = [...prev.weakTopics]
      if (!passed && !newWeakTopics.includes(topic)) {
        newWeakTopics.push(topic)
      } else if (passed) {
        newWeakTopics = newWeakTopics.filter(t => t !== topic)
      }

      return {
        ...prev,
        quizScores: newScores,
        completedChapters: newChapters,
        incorrectQuestions: newIncorrects,
        weakTopics: newWeakTopics
      }
    })
  }

  const toggleBookmark = (lessonId: string) => {
    setProgress(prev => ({
      ...prev,
      bookmarks: prev.bookmarks.includes(lessonId)
        ? prev.bookmarks.filter(b => b !== lessonId)
        : [...prev.bookmarks, lessonId]
    }))
  }

  const saveNote = (lessonId: string, noteText: string) => {
    setProgress(prev => ({
      ...prev,
      notes: {
        ...prev.notes,
        [lessonId]: noteText
      }
    }))
  }

  const recordScenarioResult = (scenarioId: string, isSuccess: boolean) => {
    setProgress(prev => ({
      ...prev,
      scenarioResults: {
        ...prev.scenarioResults,
        [scenarioId]: isSuccess
      }
    }))
  }

  const setLastLesson = (lessonId: string) => {
    setProgress(prev => ({
      ...prev,
      lastLessonId: lessonId
    }))
  }

  const resetProgress = () => {
    setProgress(initialProgress)
    localStorage.removeItem(STORAGE_KEY)
  }

  return (
    <ProgressContext.Provider
      value={{
        progress,
        markLessonComplete,
        saveQuizScore,
        toggleBookmark,
        saveNote,
        recordScenarioResult,
        setLastLesson,
        resetProgress
      }}
    >
      {children}
    </ProgressContext.Provider>
  )
}

export const useProgress = () => {
  const context = useContext(ProgressContext)
  if (!context) {
    throw new Error('useProgress must be used within a ProgressProvider')
  }
  return context
}
