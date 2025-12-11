/**
 * @jest-environment jsdom
 */

import '@testing-library/jest-dom';
import { fireEvent } from '@testing-library/dom';

describe('Notta Advisor index.html behavior', () => {
  let container: HTMLElement;

  beforeEach(() => {
    // Simulate the HTML structure needed for the tests
    document.body.innerHTML = `
      <div>
        <form id="questionForm">
          <input type="text" id="question" name="question" value="How is the tech sector performing?"/>
          <input type="hidden" name="csrfmiddlewaretoken" value="dummy_csrf_token"/>
          <button type="submit">Get Insight</button>
        </form>
        <div id="mainContent" class="lg:flex-1"></div>
        <div id="canvas" class="opacity-0 max-h-0 lg:flex-none lg:w-0">
          <div id="canvasContent"></div>
          <button id="closeCanvas"></button>
        </div>
      </div>
    `;

    // Insert the relevant JS logic from the HTML file
    document.getElementById('questionForm')!.addEventListener('submit', function(e) {
      e.preventDefault();
      const question = (document.getElementById('question') as HTMLInputElement).value;
      const canvas = document.getElementById('canvas')!;
      const canvasContent = document.getElementById('canvasContent')!;

      // Show loading
      canvasContent.innerHTML = '<div class="flex items-center justify-center h-32"><div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div></div>';

      // Show canvas
      const mainContent = document.getElementById('mainContent')!;
      canvas.classList.remove('opacity-0', 'max-h-0', 'lg:flex-none', 'lg:w-0');
      canvas.classList.add('opacity-100', 'max-h-screen', 'lg:flex-none', 'lg:w-2/3', 'lg:p-8');
      mainContent.classList.remove('lg:flex-1');
      mainContent.classList.add('lg:flex-none', 'lg:w-1/3');
    });

    document.getElementById('closeCanvas')!.addEventListener('click', function() {
      const canvas = document.getElementById('canvas')!;
      const mainContent = document.getElementById('mainContent')!;
      canvas.classList.remove('opacity-100', 'max-h-screen', 'lg:flex-none', 'lg:w-2/3', 'lg:p-8');
      canvas.classList.add('opacity-0', 'max-h-0', 'lg:flex-none', 'lg:w-0');
      mainContent.classList.remove('lg:flex-none', 'lg:w-1/3');
      mainContent.classList.add('lg:flex-1');
    });
  });

  it('has the correct initial layout for canvas and main content (canvas hidden initially)', () => {
    const canvas = document.getElementById('canvas')!;
    const mainContent = document.getElementById('mainContent')!;

    // Canvas should be hidden and have initial classes
    expect(canvas.classList.contains('opacity-0')).toBe(true);
    expect(canvas.classList.contains('max-h-0')).toBe(true);
    expect(canvas.classList.contains('lg:w-0')).toBe(true);
    expect(canvas.classList.contains('lg:flex-none')).toBe(true);

    // Main content should have initial layout class
    expect(mainContent.classList.contains('lg:flex-1')).toBe(true);
    expect(mainContent.classList.contains('lg:w-1/3')).toBe(false);
  });

  it('shows the canvas and loading spinner on form submit', () => {
    const form = document.getElementById('questionForm')!;
    fireEvent.submit(form);

    const canvas = document.getElementById('canvas')!;
    const canvasContent = document.getElementById('canvasContent')!;
    const mainContent = document.getElementById('mainContent')!;

    expect(canvas.classList.contains('opacity-100')).toBe(true);
    expect(canvas.classList.contains('max-h-screen')).toBe(true);
    expect(canvasContent.innerHTML).toContain('animate-spin');
    expect(mainContent.classList.contains('lg:w-1/3')).toBe(true);
  });

  it('hides the canvas and restores layout on close button click', () => {
    // First, show the canvas by simulating a submit
    fireEvent.submit(document.getElementById('questionForm')!);

    // Now, click the close button
    fireEvent.click(document.getElementById('closeCanvas')!);

    const canvas = document.getElementById('canvas')!;
    const mainContent = document.getElementById('mainContent')!;

    expect(canvas.classList.contains('opacity-0')).toBe(true);
    expect(canvas.classList.contains('max-h-0')).toBe(true);
    expect(mainContent.classList.contains('lg:flex-1')).toBe(true);
  });
});