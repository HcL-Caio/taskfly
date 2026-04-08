import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

test('deve renderizar o título da aplicação', () => {
  render(<App />);
  const linkElement = screen.getByText(/TaskFly/i);
  expect(linkElement).toBeInTheDocument();
});

test('deve adicionar uma nova tarefa ao clicar no botão', () => {
  render(<App />);
  const input = screen.getByPlaceholderText(/Adicione uma tarefa/i);
  const botao = screen.getByRole('button', { name: /adicionar/i });

  fireEvent.change(input, { target: { value: 'Estudar para o Bootcamp' } });
  fireEvent.click(botao);

  const tarefa = screen.getByText('Estudar para o Bootcamp');
  expect(tarefa).toBeInTheDocument();
});

test('não deve permitir adicionar tarefa vazia', () => {
  render(<App />);
  const botao = screen.getByRole('button', { name: /adicionar/i });
  fireEvent.click(botao);
  
  const tarefas = screen.queryAllByRole('listitem');
  expect(tarefas.length).toBe(0);
});
