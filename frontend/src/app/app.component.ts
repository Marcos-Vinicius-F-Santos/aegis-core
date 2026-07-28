import { Component, ElementRef, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AegisApiService } from './services/aegis-api.service';
import { Agent, ChatMessage } from './models/chat.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  @ViewChild('chatLog') private chatLogContainer!: ElementRef;

  userInput = '';
  isLoading = false;
  messages: ChatMessage[] = [];

  availableAgents: Agent[] = [
    {
      id: 'cortex',
      name: 'Cortex',
      roleTitle: 'Núcleo de Conversação',
      description: 'Especialista em diálogos, esclarecimento de dúvidas e síntese de contexto.',
      icon: '🧠',
      accentColor: '#6366f1',
      glowColor: 'rgba(99, 102, 241, 0.35)',
      badge: 'Ativo',
      systemPromptPreview: 'Núcleo de conversação geral do Aegis'
    },
    {
      id: 'cortana',
      name: 'Cortana',
      roleTitle: 'Engenharia de Software',
      description: 'Especialista em programação, revisão de código e arquitetura de sistemas.',
      icon: '⚡',
      accentColor: '#06b6d4',
      glowColor: 'rgba(6, 182, 212, 0.35)',
      badge: 'Pronto',
      systemPromptPreview: 'Assistente especialista em código'
    },
    {
      id: 'rick',
      name: 'Rick',
      roleTitle: 'Pesquisa & Dados',
      description: 'Agente focado em análise avançada de informações e investigações.',
      icon: '🔬',
      accentColor: '#f59e0b',
      glowColor: 'rgba(245, 158, 11, 0.35)',
      badge: 'Pronto',
      systemPromptPreview: 'Agente de pesquisa e dados'
    }
  ];

  selectedAgent: Agent = this.availableAgents[0];

  constructor(private aegisApi: AegisApiService) {}

  selectAgent(agent: Agent): void {
    this.selectedAgent = agent;
  }

  onKeyDown(event: Event): void {
    const kbEvent = event as KeyboardEvent;
    if (kbEvent.key === 'Enter' && !kbEvent.shiftKey) {
      event.preventDefault();
      this.sendMessage();
    }
  }

  sendQuickPrompt(promptText: string): void {
    this.userInput = promptText;
    this.sendMessage();
  }

  clearChat(): void {
    this.messages = [];
  }

  sendMessage(): void {
    const text = this.userInput.trim();
    if (!text || this.isLoading) return;

    // Add user message
    this.messages.push({
      id: 'usr-' + Date.now(),
      role: 'user',
      content: text,
      timestamp: new Date()
    });

    this.userInput = '';
    this.isLoading = true;
    this.scrollToBottom();

    this.aegisApi.sendMessage(text).subscribe({
      next: (res) => {
        this.messages.push({
          id: 'bot-' + Date.now(),
          role: 'assistant',
          content: res.response,
          agent: res.agent || this.selectedAgent.name,
          executionTime: res.execution_time,
          timestamp: new Date()
        });
        this.isLoading = false;
        this.scrollToBottom();
      },
      error: (err) => {
        this.messages.push({
          id: 'err-' + Date.now(),
          role: 'assistant',
          content: `⚠️ Erro ao se conectar com o servidor Aegis: ${err.message || 'Verifique se o backend está rodando em http://localhost:8000'}`,
          agent: 'Sistema',
          timestamp: new Date()
        });
        this.isLoading = false;
        this.scrollToBottom();
      }
    });
  }

  private scrollToBottom(): void {
    setTimeout(() => {
      if (this.chatLogContainer) {
        this.chatLogContainer.nativeElement.scrollTop = this.chatLogContainer.nativeElement.scrollHeight;
      }
    }, 50);
  }
}
