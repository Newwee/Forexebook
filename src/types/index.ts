export type Difficulty = 'Beginner' | 'Intermediate' | 'Advanced'
export type Category = 'Foundations' | 'Structure' | 'Liquidity' | 'Entry Execution' | 'Mastery'

export interface KeyTerm {
  term: string
  meaning: string
}

export interface OriginalImage {
  url: string
  caption: string
  page: number
}

export interface Lesson {
  id: string
  title: string
  content: string
  corePrinciples: string[]
  practicalExamples: string
  proTips: string
  pitfalls: string
}

export interface QuizQuestion {
  id: string
  type: 'mcq' | 'scenario' | 'chart' | 'tf'
  question: string
  options: string[]
  correctIndex: number
  explanation: string
  referenceConcept: string
}

export interface Chapter {
  id: string
  chapterNumber: number
  title: string
  englishTitle: string
  category: Category
  difficulty: Difficulty
  estimatedMinutes: number
  pdfPages: string
  shortDescription: string
  whyItMatters: string
  summary: string[]
  keyTerms: KeyTerm[]
  originalImages: OriginalImage[]
  lessons: Lesson[]
  quiz: QuizQuestion[]
}

export interface GlossaryTerm {
  id: string
  term: string
  thaiName: string
  category: Category
  definition: string
  example: string
  relatedChapterId: string
}

export interface ScenarioOption {
  id: string
  text: string
  isCorrect: boolean
  feedback: string
}

export interface Scenario {
  id: string
  title: string
  category: string
  difficulty: Difficulty
  setupDescription: string
  chartRenderUrl: string
  originalPageRef: number
  question: string
  options: ScenarioOption[]
  institutionalExplanation: string
}

export interface QuizAttempt {
  score: number
  total: number
  date: string
  passed: boolean
}

export interface IncorrectQuestionRecord {
  question: string
  yourAnswer: string
  correctAnswer: string
  explanation: string
}

export interface UserProgress {
  completedLessons: string[]
  completedChapters: string[]
  quizScores: Record<string, QuizAttempt>
  incorrectQuestions: Record<string, IncorrectQuestionRecord>
  weakTopics: string[]
  bookmarks: string[]
  notes: Record<string, string>
  streak: number
  lastActiveDate: string
  lastLessonId: string
  scenarioResults: Record<string, boolean>
}
