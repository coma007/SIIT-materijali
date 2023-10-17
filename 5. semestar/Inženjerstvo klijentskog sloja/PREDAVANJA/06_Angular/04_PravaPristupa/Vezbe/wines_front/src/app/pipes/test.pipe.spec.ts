import { TestPipe } from './test.pipe';

describe('MojPipe', () => {
	it('create an instance', () => {
		const pipe = new TestPipe();
		expect(pipe).toBeTruthy();
	});
});
